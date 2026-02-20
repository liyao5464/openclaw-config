---
name: draft-writer
description: 根据选题生成文章初稿。用于：选题确认后开始写初稿时（触发词：写初稿、开始写、生成初稿）。
---

# 初稿生成

## 关联技巧库

- **框架类型**：`../article-analyzer/references/framework-types.md`
- **开头技巧**：`../article-analyzer/references/opening-techniques.md`
- **结尾技巧**：`../article-analyzer/references/ending-techniques.md`
- **案例框架**：`../article-analyzer/references/case-frameworks.md`
- **衔接技巧**：`../article-analyzer/references/transition-techniques.md`

---

## 输入

- **必须**：项目路径（如 `./projects/my-project/`）
- **可选**：用户额外提供的素材

**首先读取项目信息**：
```
读取项目：./projects/my-project/

选题：___
评分：___/25 (X级)
素材：
├── cases/ (X 个文件)
├── quotes/ (X 个文件)
└── references/ (X 个文件)

开始写初稿...
```

---

## 工作流程

复制此清单跟踪进度：

```
初稿进度：
- [ ] 第一步：确定大框架
- [ ] 第二步：构建开头
- [ ] 第三步：填充各部分内容
- [ ] 第四步：构建结尾
```

---

### 第一步：确定大框架

**⚠️ 务必先读入**：`../article-analyzer/references/framework-types.md`

1. 提供框架选项：
```
请选择文章框架：

A. [框架名] ⭐⭐⭐ (推荐度 85%)
   理由：___
   结构预览：___

B. [框架名] ⭐⭐ (推荐度 60%)
   ...
```

2. **等待用户确认**（用户说「你选」→ 自动选最高推荐）

3. 确认后输出：
```
✅ 大框架确定

框架：[选择的框架]
结构：
├── 开头
├── 部分1：___
├── 部分2：___
├── 部分3：___
└── 结尾
```

4. **用户确认后才进入下一步**

---

### 第二步：构建开头

**⚠️ 务必先读入**：`../article-analyzer/references/opening-techniques.md`

1. 提供开头选项：
```
请选择开头方式：

A. 激发好奇心 ⭐⭐⭐ (推荐度 75%)
   - 子类型：[提问/反常观点/超出认知/新闻要点]

B. 展示价值 ⭐⭐ (推荐度 55%)
   - 子类型：[痛点描述/内容预告]

C. 与读者有关 ⭐⭐ (推荐度 50%)
   - 子类型：[直接点明受众/利益]
```

2. 用户选择大类 → 选择子类型

3. 生成开头内容

4. **等待用户确认**
   - 如果不满意：询问具体问题 → 修改 → 再次确认
   - **确认通过后才进入下一步**

---

### 第三步：填充各部分内容

对每个部分逐一构建：

1. 选择内容组织方式（先观点后案例/先案例后观点/多案例并列）

2. 检查素材
   - 如果缺失：
   ```
   ⚠️ 素材缺失
   这部分需要案例，请选择：
   1. 你有相关素材吗？（发给我）
   2. 要我帮你搜索/编造一个？
   3. 跳过这部分？
   ```

3. 选择案例框架（**务必读入** `../article-analyzer/references/case-frameworks.md`）

4. 选择衔接方式（**务必读入** `../article-analyzer/references/transition-techniques.md`）

5. 生成内容，插入配图占位符：`（配图：XXX）`

6. **等待用户确认该部分**
   - 如果不满意：修改 → 再次确认
   - **确认后继续下一部分**

7. **所有部分确认后才进入下一步**

---

### 第四步：构建结尾

**⚠️ 务必先读入**：`../article-analyzer/references/ending-techniques.md`

1. 提供结尾选项：
```
请选择结尾方式：

A. 制造共鸣 ⭐⭐⭐ (推荐度 70%)
   - 效果：读完想转发表态

B. 强化价值 ⭐⭐ (推荐度 60%)
   - 效果：读完想收藏

C. 制造话题 ⭐⭐ (推荐度 55%)
   - 效果：读完想评论讨论
```

2. 生成结尾内容

3. **等待用户确认**
   - 如果不满意：修改 → 再次确认
   - **确认通过后完成初稿**

---

## 输出

**写入项目目录**：

1. 保存路径：`[项目路径]/outputs/article/draft.md`

2. 写入文件，格式：
```markdown
---
stage: draft
created: [日期时间]
framework: [框架名]
opening: [开头技巧]
ending: [结尾技巧]
word_count: [字数]
---

# [选题/标题]

[正文内容]
```

3. 更新 `project.yaml`：
```yaml
outputs:
  article:
    stage: draft
    framework: "框架名"
    word_count: 2500
```

4. 确认输出：
```
═══════════════════════════════════════
✅ 初稿完成
═══════════════════════════════════════

已保存至：./projects/xxx/outputs/article/draft.md
字数：2500

下一步：进入润色阶段
命令：/polish-editor ./projects/xxx/
```

---

## 快速模式

用户说「快速生成」→ 跳过确认环节，自动选择推荐度最高的选项，只在素材缺失时询问，自动使用默认路径保存。
