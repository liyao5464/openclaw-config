# 微信公众号发布方法记录
## 内容总监的成功经验

**发现时间：** 2026-02-17
**关键发现：** 内容总监能发布，而我不能，原因可能是发布方式不同

---

## 发布方式对比

| 方式 | 原理 | 账号要求 | 我的尝试结果 |
|-----|------|---------|-------------|
| **API模式** | 调用微信 `draft/add` 接口 | 需要**已认证的服务号** | ❌ 40007错误（权限不足） |
| **浏览器模式** | Chrome CDP 模拟人工操作 | **任何账号**（订阅号也可） | 未尝试 |

---

## 关键结论

**我的账号状态：**
- 订阅号 + 未认证
- `qualification_verify: False`
- API模式返回 40007（invalid media_id）

**内容总监可能用的方法：**
- 浏览器模式（`wechat-article.ts` 或 `wechat-browser.ts`）
- 通过 Chrome 自动化登录公众号后台
- 模拟人工复制粘贴发布

---

## 浏览器模式使用方法

根据 baoyu-post-to-wechat SKILL.md:

```bash
# 文章模式（浏览器自动化）
npx -y bun ${SKILL_DIR}/scripts/wechat-article.ts --html article.html

# 图文模式
npx -y bun ${SKILL_DIR}/scripts/wechat-browser.ts --markdown article.md --images ./images/
```

**要求：**
- 安装 Google Chrome
- 首次运行需要扫码登录（会话会保留）
- 不需要 API 权限

---

## 下一步尝试

下次发布时，应该：
1. 使用浏览器模式而非API模式
2. 确保Chrome已安装
3. 首次运行扫码登录后，后续可自动发布

---

## 文件位置

内容总监的已发布文章存放在：
`/root/.openclaw/workspace-director/drafts/html/`

包括：
- ai-spring-festival-final.html
- baidu-openclaw-tutorial.html
- baidu-app-openclaw-full-guide.html
- 等7篇文章
