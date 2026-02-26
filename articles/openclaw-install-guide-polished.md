# 我是纯文科生，但2小时后我有了自己的AI团队（附完整踩坑实录）

Claude官方的Projects功能太鸡肋了。

上下文限制、不能同时养多个AI助手、每次切换都要重新交代背景——我用了一周就放弃了。

然后朋友跟我说了一句话，改变了一切。

"你试试OpenClaw，能养一群AI助手，每个都有自己的记忆和工具。"

我当时的反应是：哥们，我是纯文科生，一行代码都不会写，你让我"养"AI？

我连养花都养不活。

但那天下午闲着也是闲着，我就想，试试呗，大不了浪费两小时。

没想到，真的就两小时，我搞定了。

下面是我边装边崩溃边自救的完整记录。提前说好——踩的坑比走的路还多。

---

## 服务器这事，我一上来就栽了

先说你需要准备什么：一台海外服务器（腾讯云阿里云都行），一个飞书账号，一个Claude API Key（官方或中转站都行）。

我选了腾讯云轻量服务器，新加坡节点，2核4G，购买链接：https://buy.cloud.tencent.com

听起来很简单对吧？

我也是这么想的。

然后我选了上海的服务器。

装到一半，飞书webhook死活连不上。我对着屏幕发了十分钟呆，才反应过来——服务器地区要选海外的。香港、新加坡、日本，随便哪个都行，就是不能选国内。

重装系统，又浪费了1小时。

我当时就想，这才刚开始啊。

---

## 初始化倒是顺利，直到选模型那一步

连上服务器，敲下这行命令：

```bash
openclaw onboard --install-daemon
```

然后跟着向导一步步走，填信息、选配置，感觉自己像个提线木偶——它问什么我填什么，虽然有一半看不懂，但居然一路绿灯。

我甚至开始飘了。

心想：就这？文科生也能搞定嘛。

然后，到了选模型这一步，我选了kimi2.5。

报错。

换了个写法，还是报错。

我差点把键盘砸了。

后来翻了半天文档才搞明白：Kimi要选code版本，不能选普通版。

正确的是 `kimi-coding/k2p5`，而不是 `kimi/moonshot-v1`。

一字之差，天壤之别。

MiniMax更离谱。它分国内版和海外版，API Key不能混用。我在minimaxi.com申请的Key，结果配到了海外版接口，报错信息写着"401 token is unusable (1004)"。

我盯着这行英文看了五分钟，心态差点崩了。

后来才知道：国内版用 `api.minimaxi.com`，海外版用 `api.minimax.chat`，Key也是分开申请的。

谁设计的这个？出来挨打。

---

## 飞书机器人：我和权限斗智斗勇了半小时

这一段是整个过程里最折磨人的。

先去飞书开放平台创建应用：https://open.feishu.cn/app

点"创建企业自建应用"，填个名字，传个图标，拿到App ID和App Secret。

到这里都还好。

然后是配权限。

点"权限管理"→"批量导入/导出权限"，把下面这段JSON完整粘贴进去：

```json
{
  "scopes": {
    "tenant": [
      "im:message",
      "im:message.p2p_msg:readonly",
      "im:message.group_at_msg:readonly",
      "im:message:send_as_bot",
      "im:resource",
      "contact:user.base:readonly",
      "im:message.group_msg",
      "im:message:readonly",
      "im:message:update",
      "im:message:recall",
      "im:message.reactions:read"
    ]
  }
}
```

我第一次偷懒，只开了一个基础的 `im:message`，心想够用了吧。

结果机器人接入飞书后，我发消息，它不回。

再发，还是不回。

我以为是网络问题，重启了三遍服务器。

排查了整整半小时，最后发现——"接收消息"的权限没开全。

特别是这两个：
- `im:message.p2p_msg:readonly`（接收私聊消息）
- `im:message.group_at_msg:readonly`（接收群聊@消息）

少开一个，你的机器人在飞书里就是个聋子。它能说话，但听不见你说什么。

半小时，就因为少勾了两个权限。

接下来是事件订阅。点"事件与回调"→"事件配置"→订阅方式选"长连接"→添加事件→选"接收消息"。

这里有个选项叫"HTTP回调"，千万别选。选了要填URL和Token，配置巨复杂。选长连接，直接能用，别给自己找麻烦。

我就是选了HTTP回调，折腾了二十分钟才换回来的那个人。

---

## Telegram那个验证码，我试了三个手机号

如果你还想接入Telegram，流程本身不复杂。

在Telegram里搜 `@BotFather`，发 `/newbot`，按提示设个名字和ID，拿到Token。格式长这样：`123456789:ABCdefGHIjklMNOpqrSTUvwxyz`

然后把配置发给OpenClaw（飞书或命令行都行）：

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "你的Bot Token"
    }
  }
}
```

技术上就这么简单。

但Telegram本身的注册，是个玄学。

iPhone用户需要美区Apple ID才能下载。注册需要境外手机号，或者国内手机号碰运气。

我试了3个手机号。

第一个，验证码没来。

第二个，还是没来。

我开始怀疑人生。

最后用了Google Voice的虚拟号，终于收到了。安卓用户相对容易些，但也得有梯子。

这一步跟技术无关，纯粹是跟运气较劲。

---

## 插件打架这事，真的会发生

配置过程中我执行了：

```bash
openclaw plugins add feishu
```

装好了，能用了。

然后我不知道哪根筋搭错了，又手动装了一遍：

```bash
npm install @larksuiteoapi/node-sdk
```

从此每次启动都报错：

```
Config warnings: plugin feishu: duplicate plugin id detected
```

我当时完全懵了。什么叫duplicate？我装了两遍？

是的，我装了两遍。

解决方法是删掉全局那个多余的：

```bash
sudo rm -rf /root/.nvm/versions/node/v24.7.0/lib/node_modules/openclaw/extensions/feishu
```

只保留 `~/.openclaw/extensions/feishu` 这一个就行。

一个插件装两遍这种蠢事，大概只有我干得出来。

---

## 最后一步，别忘了切模型

全部配完，重启网关：

```bash
openclaw gateway restart
```

然后在飞书里对机器人说：

```
/model kimi-coding/k2p5
```

或者：

```
/model minimax/MiniMax-M2.5
```

我当时没切模型，直接跟机器人说话。

它报错了。

因为默认模型是Claude，我又没配官方API。相当于你点了外卖，但没填地址。

切到国内模型就好了。这个坑不大，但踩上去也挺烦的。

---

## 三个救命命令，记好了

整个过程中，我反复用到这三个命令。可以说，没有它们我早就放弃了：

```bash
# 查看状态
openclaw gateway status

# 重启网关
openclaw gateway restart

# 自动修复
openclaw doctor --fix
```

90%的问题，重启一下就好了。

如果重启后看到绿色的 `RPC probe: ok`，深呼吸，你成功了。

---

## 两小时后的我

现在我有7个Agent。

每个都有自己的记忆，自己的性格，自己的活儿。

一个帮我统筹全局，日常沟通。一个当内容总监，审核文章、排版公众号。一个是育儿师，记录宝宝的成长。一个管视频脚本和分镜。还有专门写Twitter的、写微博小红书的、甚至还有个"AI华佗"帮我查育儿医学知识。

7个。

我一个文科生，搞出了一个7人AI团队。

每天早上打开飞书，看到"开发者小助手"的绿色在线标志，我都会愣一下。

不是因为它有多厉害。

是因为我居然真的做到了。

两小时前我还在想"算了吧，我又不是程序员"。两小时后我坐在这里，看着7个AI各司其职，觉得有点不真实。

整个过程狼狈吗？

狼狈。

选错服务器、配错模型、权限漏开、插件装两遍、验证码收不到——每一步都在提醒我：你是个外行。

但外行怎么了。

外行也能把事情搞定。只不过多摔几跤，多骂几句，多重启几次。

如果你现在也在犹豫，觉得自己"不是搞技术的料"——

我两小时前也是这么想的。
