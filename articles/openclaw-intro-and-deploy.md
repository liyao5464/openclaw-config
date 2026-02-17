# OpenClaw是什么？我花30分钟搭了一个24小时在线的AI助理

> 不用写代码，每月一杯奶茶钱，拥有一个完全属于你的AI助理。

最近老有朋友问我："你那个每天自动发AI新闻的机器人是怎么搞的？"

今天统一回答一下：用的**OpenClaw**。

这玩意儿挺有意思，简单来说就是**开源版的ChatGPT Plus，但是跑在你自己的服务器上**。

你可以把它理解成一个"AI助理操作系统"——装上之后，你就能拥有一个24小时在线、会定时提醒、能接入微信/钉钉/飞书、而且数据完全私有的AI助理。

最重要的是：**真的不需要写代码**，跟着步骤点点鼠标就行。

下面是我踩过坑之后整理的保姆级教程。

---

## OpenClaw能干嘛？

先说说我用OpenClaw实现了哪些功能：

**1. 每日AI早报**

每天早上7:30，我的AI助理自动搜索昨天的AI新闻，筛选3-5条重要的，推送到我的微信。

不用我手动去翻Twitter、刷知乎，醒来拿起手机就能看到。

**2. 定时提醒**

- 每周一早上提醒写周报
- 每月1号提醒交房租
- 每年朋友生日提前3天提醒

这些以前都要靠闹钟或者备忘录，现在AI到点就发消息，比闹钟温柔多了。

**3. 跨平台消息管理**

我在Telegram、飞书、微信都有群，有时候消息看不过来。

现在可以让AI帮我：
- 把重要的消息从一个平台转发到另一个
- 统一回复常见问题
- 自动整理群聊要点

**4. 个人知识库**

有什么重要信息直接发给AI，它会记下来。

之后可以随时问："我之前说的那个xxx在哪？" "上周三的会议纪要发我一下"

**5. 数据完全私有**

这是我最看重的一点。

ChatGPT、Claude这些虽然好用，但聊天记录都存在别人的服务器上。有些敏感信息（比如商业计划、账号密码）我不太放心往上扔。

OpenClaw部署在你自己的服务器上，数据完全属于你，不用担心被拿去训练模型，也不用担心突然哪天服务就关了。

---

## OpenClaw是什么原理？

一句话解释：**它是一个AI助理的"操作系统"**。

传统的AI对话（比如ChatGPT），你发一条消息，它回一条，聊完就完了。

OpenClaw不一样，它会**一直运行在你的服务器上**，可以：
- 定时执行任务（比如每天早上7点发新闻）
- 接入多个消息平台（微信、钉钉、飞书、Telegram）
- 记住你的偏好和过往对话
- 通过"技能"扩展功能（天气查询、RSS订阅、股票查询等）

你可以把它想象成一个**7×24小时在线的数字员工**，只为你一个人服务。

---

## 部署OpenClaw需要什么？

| 项目 | 干嘛用的 | 花多少钱 |
|------|---------|---------|
| 一台云服务器 | 跑OpenClaw程序 | 新用户首月免费，之后约50元/月 |
| 一个AI模型API Key | 让AI能说话 | Kimi免费额度够用 |
| 一双手 | 复制粘贴命令 | 免费 |

**云服务器选哪家？**

腾讯云、阿里云、百度云都可以。这里以**百度云**为例，新用户有免费试用，而且百度云的轻量服务器对新手比较友好。

配置选**2核2G4M带宽**就够了，一个月50块钱左右，比ChatGPT Plus便宜。

---

## 部署教程（30分钟搞定）

### 第一步：买服务器（5分钟）

1. 打开[百度云官网](https://cloud.baidu.com)，注册账号
2. 进控制台 → 轻量应用服务器 → 新建
3. 配置这么选：
   - **地域**：选离你近的（比如北京、广州）
   - **镜像**：Ubuntu 22.04（别选CentOS，命令不好记）
   - **套餐**：2核2G4M带宽，够用了
   - **时长**：1个月（新用户有免费额度）
4. 点购买，等1分钟创建完成

创建好后，记下这些信息：
- **公网IP**：比如`123.45.67.89`
- **用户名**：默认`root`
- **密码**：你自己设的

### 第二步：连上服务器（5分钟）

**Windows用户：**
1. 下载[PuTTY](https://www.putty.org/)（免费SSH工具）
2. Host Name填服务器IP，Port填22
3. 点Open，输入用户名`root`和密码

**Mac用户：**
打开终端，输入：
```bash
ssh root@你的服务器IP
```

看到下面这行字就说明连上了：
```
root@VM-0-11-ubuntu:~#
```

### 第三步：安装OpenClaw（10分钟）

下面的命令直接复制粘贴就行。

**1. 安装Node.js**
```bash
# 更新软件源
apt update

# 安装Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

# 检查安装
node -v
npm -v
```

**2. 安装OpenClaw**
```bash
# 全局安装
npm install -g openclaw

# 验证
openclaw --version
```

**3. 运行配置向导**
```bash
openclaw wizard
```

跟着提示选：
- Install mode: **local**（本地模式）
- LLM provider: **kimi-coding**（国内访问快）
- API Key: 输入你的Kimi API Key
- Channels: 勾选**telegram**和**feishu**（建议两个都选）

**Kimi API Key怎么获取？**

打开[Kimi开放平台](https://platform.moonshot.cn) → 注册账号 → 创建API Key → 复制即可。新用户有免费额度。

**4. 启动服务**
```bash
openclaw gateway start
```

看到`Gateway started on port 18789`就说明启动成功了。

### 第四步：接入消息平台（10分钟）

OpenClaw支持接入微信、钉钉、飞书、Telegram等多个平台。

**新手建议先从Telegram或飞书开始**，这俩最简单。

**方案A：Telegram（最简单）**

1. 在Telegram搜索`@BotFather`
2. 发送`/newbot`创建机器人
3. 按提示输入名称和用户名
4. 复制给你的Token（格式`123456:ABC-DEF...`）
5. 配置OpenClaw：
```bash
openclaw config set channels.telegram.enabled=true
openclaw config set channels.telegram.botToken=你的Token
```
6. 给机器人发条消息测试

**方案B：飞书（国内用户推荐）**

1. 打开[飞书开放平台](https://open.feishu.cn)
2. 创建企业自建应用
3. 记录**App ID**和**App Secret**
4. 配置：
```bash
openclaw config set channels.feishu.enabled=true
openclaw config set channels.feishu.appId=你的AppID
openclaw config set channels.feishu.appSecret=你的AppSecret
```
5. 把机器人添加到飞书群或发给个人

**微信能接吗？**

个人微信比较麻烦，容易被封号。建议用**企业微信**，配置方法和飞书类似。

### 第五步：测试一下

给你的机器人发：
```
你好
```

如果它回复你，恭喜，部署成功！🎉

试试设置一个定时任务：
```bash
openclaw cron add \
  --name "早安提醒" \
  --schedule "0 8 * * *" \
  --message "早上好！今天也要加油哦~"
```

这样每天早上8点，你就会收到AI的早安消息。

---

## 进阶玩法

**安装技能扩展**
```bash
openclaw skills install weather   # 天气查询
openclaw skills install rss       # RSS订阅
openclaw skills install stock     # 股票查询
```

**设置定时任务**
```bash
# 每天早上7:30发AI新闻
openclaw cron add \
  --name "AI早报" \
  --schedule "30 7 * * *" \
  --message "搜索昨天AI大模型新闻，总结3-5条"
```

**配置记忆功能**
告诉AI你的偏好，比如"我喜欢在早上收到新闻""我是做AI科普的博主"，它会记住并在后续对话中使用。

---

## 常见问题

| 问题 | 解决方法 |
|------|---------|
| 连不上服务器 | 百度云控制台→安全组→添加22端口 |
| OpenClaw启动失败 | 先`openclaw gateway stop`再启动 |
| 收不到消息 | 检查Token/AppID是否填对 |
| AI回复慢 | Kimi免费额度用光，等明天重置或充值 |
| 定时任务不执行 | 时区不对，运行`timedatectl set-timezone Asia/Shanghai` |

---

## 写在最后

说实话，第一次部署的时候我折腾了快1个小时，主要是各种配置不熟悉。

但第二次帮朋友部署，20分钟就搞定了。

现在我的AI助理已经跑了3个多月，每天早上准时发新闻，每周提醒我写周报，有时候我忘了某件事情还会主动问我。

最重要的是，**它真的只属于我**。数据在我自己的服务器上，隐私有保障，也不用担心服务突然关停。

如果你也想拥有一个24小时在线、完全私人的AI助理，不妨花30分钟试试。

有问题随时留言，看到都会回。

---

**资源推荐**
- OpenClaw官网：https://openclaw.ai
- 官方文档：https://docs.openclaw.ai
- GitHub：https://github.com/openclaw/openclaw

---

*这篇文章首发在我的公众号「老里的一人公司」，如果对你有帮助，欢迎转发给需要的朋友。*
