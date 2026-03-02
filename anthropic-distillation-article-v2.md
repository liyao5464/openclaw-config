# Anthropic 这条推文，评论区翻车了

昨天半夜刷推，看到 Anthropic 官方发了条挺狠的指控：

> "我们发现 DeepSeek、Moonshot AI、MiniMax 对我们发起了工业级蒸馏攻击。这帮人造了 2.4 万个假账号，跟 Claude 聊了 1600 万轮，然后把 Claude 的能力偷去训练他们自己的模型。"

好家伙，直接点名三家中国公司，还把"蒸馏"这个词包装成了"攻击"。

我本来以为评论区会是"Anthropic 干得漂亮"、"支持维权"之类的，结果点进去一看——

**大型翻车现场。**

---

## 评论区第一高赞："蒸馏怎么就成了偷？"

**251 个赞，评论就一句话：**

> "HOW IS MODEL DISTILLATION STEALING 😭😭"

（翻译：模型蒸馏怎么就成了偷窃，哭哭）

这条评论能冲顶，说明大家心里都有数：蒸馏这玩意儿，AI 圈子里谁没用过？Hinton 老爷子 2015 年的论文，开源社区玩了多少年了。OpenAI、Google、Meta 都发论文教你怎么蒸馏，现在 Anthropic 突然说这是"攻击"？

更狠的在下面。

---

## "你们自己不也是靠爬全网数据起家的？"

这条评论我给满分：

> "Anthropic 花 80 亿美元未经许可训练 Claude，DeepSeek 花 0 美元未经许可训练 Claude。Anthropic 生气是因为有人用更便宜的方式玩了他们自己的游戏。"

扎心了。Anthropic 自己也是靠爬互联网数据训练的，那些数据的创作者——写博客的、拍照片的、码代码的——谁收到过一分钱？

现在轮到别人用他们的输出了，就开始喊"攻击"了。

还有更直接的：

> "didn't y'all steal the entire internet to train?"
> （你们不也偷了整个互联网来训练吗？）

> "Company that stole all the work of everyone who's ever posted anything online has thoughts on people stealing stuff"
> （偷了所有在网上发过东西的人的作品的公司，现在对偷东西的人有意见了）

**双标，这俩字写在脸上了。**

---

## 前 GitHub 员工来爆料了

这条评论我一开始以为是段子，结果越看越真：

> "我在 GitHub 工作的时候，我们不得不让你们停止过度使用我们的 API，因为你们违反 ToS 爬 GitHub 仓库。你们道了歉，然后继续这么做。"

署名是 @igorcosta，自称是前 GitHub 员工。

如果这是真的，那 Anthropic 这条推文就变成了经典的"五十步笑百步"——你自己当年爬别人数据的时候可不是这个态度。

---

## 最灵魂的一问："他们可是付了钱的"

这条评论 121 赞，简单粗暴：

> "so are they like paying customer here or whats up"
> （所以他们算是付费客户还是怎么回事？）

对啊， Anthropic 说人家搞了 2.4 万个"虚假账号"——但如果这些账号是正常注册、正常付 API 钱的，那凭什么是"虚假"？

用户付了钱，按照你的 ToS 调 API，怎么突然就成"欺诈"了？

另一条评论把这个逻辑推到了极致：

> "When you guys train your model by bombarding others for free of cost, it's fine. But if others are training by paying your model, it's illegal? Unethical?"
> 
> （你们免费爬别人数据训练就行，别人付费用你的模型训练就违法？就不道德？）

**逻辑闭环，无解。**

---

## GDPR 警告：你们能追踪用户身份？

有个欧盟用户抓住了 Anthropic 话里的一个细节，展开了灵魂拷问。

Anthropic 原文说：
> "By examining request metadata, we were able to trace these accounts to specific researchers at the lab."
> （通过检查请求元数据，我们能够将这些账号追踪到实验室的具体研究人员。）

这位用户直接开炮：

> "所以……你们在炫耀你们能用元数据去匿名化用户？这是你们的隐私宣传口径吗？"

然后连珠炮似的追问：
1. 你们处理了哪些具体的"请求元数据"？
2. 根据 GDPR 第 6 条，这种处理的法律依据是什么？
3. 欧盟用户是否被告知（第 13/14 条）？
4. 这种元数据是否用于用户级别的归因/追踪？

**这招狠啊，直接搬出 GDPR。** 要是 Anthropic 真的用元数据追踪用户身份，那在欧盟可能面临巨额罚款。

---

## 评论区在玩梗

除了正经撕逼，评论区也是 meme 大战。

**最毒舌的双关：**
> "Rename Moonshot to Moonshine, it's illegally distilled"
> （把 Moonshot 改名 Moonshine 吧，这是非法蒸馏的）

Moonshine（私酿酒）和 Moonshot 押韵，完美呼应了"蒸馏"这个梗。我笑了半天。

**最萌的：**
> "Mom, the models are fighting"
> （妈妈，AI 模型们打起来了）

**最技术的：**
> "Ask Kimi K2.5 who it is with a temperature > 0 and it will tell you it's Claude"
> （问 Kimi K2.5 它是谁，温度调高点，它会告诉你它是 Claude）

这条暗示月之暗面的 Kimi 可能是蒸馏 Claude 出来的，温度高了就"露馅"。44 个赞。

**最扎心的：**
> "It sucks to have your art scraped and stolen by an AI company doesn't it…"
> （被 AI 公司抓取和窃取作品的感觉很糟糕，对吧……）

这条评论获得大量点赞。讽刺之处在于：这正是无数艺术家、作家、程序员对 Anthropic 等 AI 公司说过的话。

**现在轮到 AI 公司体验这种感觉了。**

---

## 那条"国家安全"的评论

在一片嘲讽声中，也有严肃的声音：

> "很多人认为是双标，但我们真的应该担心中国能用这种方式窃取美国前沿 AI 研究，这是国家安全问题，不只是版权。"

这条代表了美国科技界的另一种焦虑。技术竞争上升到国家战略层面，这已经不只是一个商业纠纷了。

但我看评论区大多数人并不买账这个叙事。毕竟，"国家安全"这张牌打太多了，大家已经审美疲劳。

---

## 这事儿到底咋回事？

说白了，Anthropic 想打舆论战，结果把自己搭进去了。

他们想表达的是：**别人用 2.4 万个账号海量调用我们的 API，把 Claude 的"知识"蒸馏走，这是不正当竞争。**

但评论区不买账的原因是：**你自己当年爬全网数据的时候，问过那些创作者的意见吗？**

这就像一个人偷了全世界的书，开了个图书馆收费，然后 complaining 别人抄了他的读书笔记。

**关键在于，这个边界到底在哪？**

- 学术界的蒸馏：公开论文，小模型学大模型，没问题
- Anthropic 的指控：大规模 API 调用，"窃取"核心能力，有问题
- 但问题是：如果你的 API 是公开卖的，用户付了钱，你凭什么说人家"窃取"？

除非 Anthropic 的 ToS 里明确写了"禁止用 API 输出训练竞争模型"，否则这个指控就很站不住脚。

---

## 三家中国公司被点名

DeepSeek、Moonshot AI（月之暗面）、MiniMax。

这三家有个共同点：都在短时间内搞出了跟 Claude 差不多的能力，而且成本看起来低得离谱。

Anthropic 的潜台词是：**你们不是独立研发的，是抄我们的。**

但评论区有人说了一句大实话：

> "DeepSeek V4 要发布了，Anthropic 慌了才放出这种假指控。"

是不是"假指控"不知道，但"慌了"可能是真的。

---

## 最后说两句

我看完整条推文的评论区，最大的感受是：**AI 行业的道德高地，其实 everybody 都在抢。**

Anthropic 想占领"我们是受害者"的道德高地，结果评论区把他拉下来：**你先解释一下你自己当年爬数据的事。**

这就像一个泥潭， everybody 都在里面，谁也不比谁干净。

但 Anthropic 这条推文最有价值的地方，恰恰是它成了一个**社会实验**——它让我们看到了全球 AI 社区对"数据所有权"、"模型训练伦理"、"中美 AI 竞争"这些议题的真实态度。

**大多数人的态度是：双标狗，滚。**

当然，也有少部分人真的在担心国家安全、技术窃取。但这部分声音在评论区被淹没了。

**最后的最后，用一条评论总结这场风波：**

> "If it's real, why is this on X and not in court?"
> （如果是真的，为什么发在 X 上而不是上法庭？）

好问题。如果 Anthropic 真的有证据，为什么不直接起诉？发推文的目的是什么？

**造势，大于维权。**

而这，可能就是评论区翻车的原因。

---

*本文基于 Anthropic 官方推文及评论区公开内容整理。抓取工具：x-tweet-fetcher + Camofox。文章观点不代表本人立场，只是记录和转述。*
