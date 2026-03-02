# OpenClaw Token 优化方案
## 基于 QMD 架构的本地化文档检索系统

---

## 核心优化策略

### 1. 混合检索架构（Hybrid RAG）
```
用户查询 → 查询扩展 → BM25检索 + 向量检索 → RRF融合 → Top30重排 → 返回结果
```

| 阶段 | 技术 | Token 消耗 | 作用 |
|-----|------|-----------|------|
| 检索 | BM25 (SQLite FTS5) | 0 | 快速关键词匹配 |
| 检索 | 本地向量嵌入 | 0 | 语义相似度匹配 |
| 融合 | RRF 算法 | 0 | 合并多路召回结果 |
| 重排 | 本地重排模型 | 0 | 仅对 Top30 精排 |
| 生成 | LLM 回答 | 大幅降低 | 只处理相关上下文 |

### 2. 智能分块（Smart Chunking）
- **分块大小**：900 tokens（平衡信息密度和检索精度）
- **重叠率**：15%（保证上下文连贯）
- **边界检测**：按 Markdown 结构切割（标题、段落、代码块）
- **评分算法**：
  ```
  最终分数 = 基础分数 × (1 - (距离/窗口)² × 0.7)
  ```

### 3. 查询扩展（Query Expansion）
- 原始查询 ×2 权重
- LLM 生成 1-2 个语义变体
- 并行检索，RRF 融合

### 4. 位置感知融合（Position-Aware Blending）
| 排名 | RRF 权重 | 重排权重 | 说明 |
|-----|---------|---------|------|
| 1-3 | 75% | 25% | 保护头部精确匹配 |
| 4-10 | 60% | 40% | 平衡检索和重排 |
| 11-30 | 40% | 60% | 更依赖重排模型 |

---

## 实现方案

### 阶段一：本地嵌入模型（已完成 ✅）
使用已有的本地模型能力：
- 嵌入：Gemma 300M 或 BGE 模型
- 重排：Qwen3-Reranker 0.6B

### 阶段二：SQLite + 向量索引
```sql
-- 文档表
CREATE TABLE documents (
    id TEXT PRIMARY KEY,           -- 6字符哈希
    path TEXT NOT NULL,            -- 文件路径
    content TEXT NOT NULL,         -- 完整内容
    title TEXT,                    -- 提取的标题
    created_at INTEGER             -- 创建时间
);

-- FTS5 全文索引
CREATE VIRTUAL TABLE documents_fts USING fts5(
    content, title,
    content='documents',
    content_rowid='rowid'
);

-- 向量索引 (使用 sqlite-vec)
CREATE VIRTUAL TABLE content_vectors USING vec0(
    embedding float[768]  -- 根据模型维度调整
);

-- 上下文表
CREATE TABLE contexts (
    path TEXT PRIMARY KEY,
    description TEXT       -- 路径描述，帮助检索
);
```

### 阶段三：核心算法实现

#### 3.1 智能分块算法
```python
def smart_chunk(content: str, target_tokens: int = 900, overlap: float = 0.15):
    """
    按语义边界智能分块
    """
    break_scores = {
        '# ': 100,      # H1
        '## ': 90,      # H2
        '### ': 80,     # H3
        '```': 80,      # 代码块
        '---': 60,      # 分隔线
        '\n\n': 20,     # 空行
    }
    
    chunks = []
    window_size = int(target_tokens * overlap)
    
    # 查找最佳切割点...
    # 返回 chunks，每个包含：hash, seq, pos, text
```

#### 3.2 RRF 融合算法
```python
def rrf_fusion(results_lists: list, k: int = 60, original_boost: float = 2.0):
    """
    Reciprocal Rank Fusion
    """
    scores = defaultdict(float)
    
    for query_idx, results in enumerate(results_lists):
        weight = original_boost if query_idx == 0 else 1.0
        for rank, doc in enumerate(results):
            doc_id = doc['id']
            # RRF 公式: score += weight / (k + rank)
            scores[doc_id] += weight / (k + rank + 1)
            
            # 头部奖励
            if rank == 0:
                scores[doc_id] += 0.05
            elif rank <= 2:
                scores[doc_id] += 0.02
    
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
```

#### 3.3 查询扩展
```python
async def expand_query(query: str, llm) -> list:
    """
    生成查询变体
    """
    prompt = f"""Generate 1-2 alternative search queries for: {query}
    Keep the core meaning but vary the wording."""
    
    response = await llm.complete(prompt)
    variations = [query] + parse_variations(response)
    return variations
```

---

## 实施计划

### Week 1: 基础架构
- [ ] 创建 `smart-memory` skill
- [ ] 实现 SQLite + FTS5 索引
- [ ] 实现智能分块
- [ ] 集成本地嵌入模型

### Week 2: 混合检索
- [ ] 实现 BM25 检索
- [ ] 实现向量检索
- [ ] 实现 RRF 融合
- [ ] 实现查询扩展

### Week 3: 重排与优化
- [ ] 集成本地重排模型
- [ ] 实现位置感知融合
- [ ] 性能测试与调优
- [ ] 对比测试（原始 vs 优化）

### Week 4: 集成到 OpenClaw
- [ ] 替换现有 memory_search
- [ ] 添加增量更新机制
- [ ] 文档和示例
- [ ] 发布到 ClawHub

---

## Token 节省预估

| 场景 | 原始方式 | 优化后 | 节省 |
|-----|---------|-------|------|
| 检索 100 篇文档 | 100K tokens | Top10: 9K tokens | 91% |
| 嵌入生成 | API 调用 | 本地模型 | 100% |
| 重排处理 | 全部文档 | Top30 | 70% |
| 日常对话上下文 | 全量记忆 | 精准召回 | 50-80% |

---

## 下一步

要我帮你：
1. **创建 smart-memory skill 框架**？
2. **先实现一个简化版**（只有 BM25 + 向量）？
3. **对比测试现有 memory_search**？

选一个，我开始写代码！🦐
