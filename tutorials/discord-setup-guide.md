# Discord 接入详细教程

> 将 OpenClaw 接入 Discord，让 AI 助手在 Discord 服务器中收发消息。

---

## 一、前置条件

1. 有一个 Discord 账号
2. 有创建 Discord 服务器的权限（或已有服务器）
3. OpenClaw Gateway 已运行

---

## 二、创建 Discord Bot

### 步骤 1：进入 Discord Developer Portal

1. 访问 [Discord Developer Portal](https://discord.com/developers/applications)
2. 登录你的 Discord 账号

### 步骤 2：创建 Application

1. 点击右上角 **"New Application"**
2. 输入应用名称（如：老里AI助手）
3. 勾选服务条款，点击 **Create**

### 步骤 3：添加 Bot 用户

1. 在左侧菜单点击 **"Bot"**
2. 点击 **"Add Bot"** 按钮
3. 确认弹窗："Yes, do it!"

### 步骤 4：配置 Bot 权限

1. 在 Bot 页面，找到 **Privileged Gateway Intents**
2. 开启以下权限：
   - ✅ **MESSAGE CONTENT INTENT**（必须，否则无法读取消息内容）
   - ✅ SERVER MEMBERS INTENT（可选，如果需要成员列表）
   - ✅ PRESENCE INTENT（可选，如果需要在线状态）
3. 点击 **Save Changes**

### 步骤 5：获取 Bot Token

1. 在 Bot 页面，找到 **Token** 区域
2. 点击 **Reset Token** 或 **Copy**
3. **⚠️ 重要**：这个 Token 只显示一次，务必保存好！格式类似：
   ```
   MTAxMjM0NTY3ODkwMTIzNDU2Nzg5MA.GxYzaA.abc123_def456_ghi789
   ```

---

## 三、邀请 Bot 加入服务器

### 步骤 1：生成邀请链接

1. 在左侧菜单点击 **"OAuth2"** → **"URL Generator"**
2. 在 **SCOPES** 中勾选：
   - ✅ `bot`
   - ✅ `applications.commands`（可选，如果要使用斜杠命令）
3. 在 **BOT PERMISSIONS** 中勾选：
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ View Channels
   - ✅ Add Reactions（可选）
   - ✅ Manage Messages（可选，如果需要删除消息）
   - ✅ Attach Files（可选，如果需要发图片）

### 步骤 2：复制生成的 URL

页面底部会生成一个 URL，类似：
```
https://discord.com/api/oauth2/authorize?client_id=123456789&permissions=3136&scope=bot
```

### 步骤 3：邀请 Bot

1. 复制 URL 到浏览器打开
2. 选择要添加的服务器
3. 点击 **Continue** → **Authorize**
4. 完成人机验证（CAPTCHA）

5. 回到 Discord，你应该看到 Bot 已加入服务器

---

## 四、配置 OpenClaw

### 步骤 1：配置 Discord Token

在 OpenClaw 配置中添加 Discord Token：

```bash
# 方法1：使用 openclaw config 命令
openclaw config set channels.discord.token "你的_BOT_TOKEN"

# 方法2：直接编辑配置文件
# 文件位置：~/.openclaw/config.json
```

配置文件示例：
```json
{
  "channels": {
    "discord": {
      "token": "MTAxMjM0NTY3ODkwMTIzNDU2Nzg5MA.GxYzaA.xxxxxx",
      "actions": {
        "roles": false,
        "moderation": false,
        "presence": false,
        "channels": false
      }
    }
  }
}
```

### 步骤 2：重启 Gateway

```bash
openclaw gateway restart
```

### 步骤 3：验证连接

检查 Discord 是否连接成功：
```bash
openclaw status
```

应该看到类似输出：
```
🎮 discord   connected   @老里AI助手#1234
```

---

## 五、获取 Channel ID

要让 AI 在特定频道发送消息，需要获取 Channel ID：

### 方法 1：Discord 客户端开启开发者模式

1. Discord 设置 → Advanced → Developer Mode（开启）
2. 右键点击频道名称 → Copy Channel ID

### 方法 2：使用 openclaw directory 命令

```bash
openclaw directory
```

会列出所有可访问的 Discord 频道和 ID。

---

## 六、测试发送消息

### 命令行测试

```bash
openclaw message send "你好，Discord！" --channel discord --to "channel:频道ID"
```

### Agent 中发送

在 agent 对话中，直接说：
```
发消息到 Discord："你好，服务器的朋友们！"
```

或者在 skill 中使用：
```json
{
  "action": "send",
  "channel": "discord",
  "to": "channel:1234567890",
  "message": "Hello Discord!"
}
```

---

## 七、常见问题

### Q1: Bot 不响应消息
- 检查 MESSAGE CONTENT INTENT 是否开启
- 检查 Bot 是否有 Read Message History 权限
- 确认 Bot 在正确的频道中

### Q2: 无法发送消息
- 检查 Bot 是否有 Send Messages 权限
- 确认 Token 配置正确
- 检查 Gateway 日志：`openclaw logs`

### Q3: 如何私信用户
```json
{
  "action": "send",
  "channel": "discord",
  "to": "user:用户ID",
  "message": "私信内容"
}
```

### Q4: 如何 @ 用户
在消息中使用 `<@用户ID>`：
```
Hello <@123456789>!
```

---

## 八、安全建议

1. **Token 保密**：不要将 Bot Token 提交到 GitHub 或分享给他人
2. **权限最小化**：只给 Bot 必要的权限
3. **定期轮换**：定期重置 Token（Discord Bot 页面 → Reset Token）

---

## 九、进阶配置

### 多服务器支持
OpenClaw 支持一个 Bot 在多个服务器中使用，只需确保 Bot 已加入所有目标服务器。

### 使用 Slash Commands
如需使用 Discord 斜杠命令，需要在 OAuth2 URL Generator 中勾选 `applications.commands`，并在代码中注册命令。

### 监听消息事件
默认配置下，OpenClaw 可以：
- 接收 @提及 Bot 的消息
- 接收 DM（私信）消息
- 在配置了 webhook 的频道中接收所有消息

---

**完成！** 现在 OpenClaw 已成功接入 Discord 🎮
