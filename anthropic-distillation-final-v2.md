# Anthropic 急了？一条推文暴露的 AI 霸权焦虑

昨天半夜刷推，Anthropic 官方突然发了条措辞严厉的指控：

> "我们发现 DeepSeek、Moonshot AI、MiniMax 对我们发起了工业级蒸馏攻击。这帮人造了 2.4 万个假账号，跟 Claude 聊了 1600 万轮，然后把 Claude 的能力偷去训练他们自己的模型。"

好家伙，直接点名三家中国公司。但仔细看这条推文，我第一反应不是"Anthropic 好惨"，而是——

**你们是不是有点太紧张了？**

---

## 一个细思极恐的细节

Anthropic 在推文里把三家公司按这个顺序排列：
- DeepSeek（深度求索）
- Moonshot AI（月之暗面）
- MiniMax

但看看实际调用数据：
- **DeepSeek**: 15 万次
- **Moonshot AI**: 340 万次  
- **MiniMax**: 1300 万次

**发现问题了吗？**

调用量最少的 DeepSeek 被摆在第一位，调用量最大的 MiniMax 反而排在最后。

这不是按调用量排序，这是按**威胁程度**排序。

**Anthropic 最忌惮的，不是调用最多的，而是进步最快的。**

DeepSeek V2 那惊人的性价比，显然给 Anthropic 留下了深刻印象。15 万次调用就能造成这么大的威胁，这说明什么？

**说明 DeepSeek 的效率太高了，高到让 Anthropic 感到恐惧。**

---

## 马斯克的神回复

马斯克在这条推文下回复了两个字：

> **"Banger"** 🤣

（翻译：神回复/经典发言）

然后他又补了一句：

> **"How dare they steal the stuff Anthropic stole from human coders??"**
> 
> （他们怎么敢偷 Anthropic 从人类程序员那里偷来的东西？？）

**这话太毒了。**

短短一句话，道出了整个 AI 行业的荒诞：
- Anthropic 爬全网数据训练模型 → 叫"创新"
- 别人调用 API 学习 Claude 的输出 → 叫"偷窃"

**双标，写在脸上了。**

---

## 1600 万轮？中转 API 都不止这么多

Anthropic 特意强调"1600 万轮对话"，想说明规模有多大。但等等——

**1600 万轮很多吗？**

对于做模型蒸馏的团队来说，这个数字真的不算夸张。一个中等规模的中文 AI 应用，日活用户聊个几百万轮很正常。更何况 DeepSeek 这种级别的团队，调用量只会更大。

而且 Anthropic 回避了一个关键问题：这些账号是**付费**的。

如果 DeepSeek 们是正常注册、正常充值、正常调 API，那 Anthropic 收了钱，转头说人家"欺诈"？

这逻辑就像是：开饭店的收了客人饭钱，然后抱怨"你们吃太多了，把我们的菜谱偷走了"。

**不是，你 API 定价的时候没算过成本吗？**

---

## 评论区的大型翻车现场

我原以为评论区会是"Anthropic 干得漂亮"，结果点进去一看——

**清一色的嘲讽。**

最高赞现在已经涨到 **290 赞**，就一句话：

> "HOW IS MODEL DISTILLATION STEALING 😭😭"

（模型蒸馏怎么就成了偷窃，哭哭）

底下有人算账：

> "Anthropic 花 80 亿美元未经许可训练 Claude，DeepSeek 花 0 美元未经许可训练 Claude。Anthropic 生气，是因为有人用更便宜的方式玩了他们自己的游戏。"

更狠的是前 GitHub 员工实名爆料：

> "我在 GitHub 工作的时候，我们不得不让你们停止过度使用我们的 API，因为你们违反 ToS 爬 GitHub 仓库。你们道了歉，然后继续这么做。"

**五十步笑百步，现场直播。**

---

## 经济学视角：寻租行为

有位经济学背景的评论者说得特别好：

> "Calling this an 'attack' is interesting. In economics we call this **competitive learning spillover**. When you train on the world's data but object to others learning from your outputs, that's simply **rent-seeking behavior**... Innovation loves competition. **Moats hate it.**"

翻译一下：
- **竞争性学习溢出** - 正常的商业现象，知识自然会扩散
- **寻租行为** - 不靠创新，靠设置壁垒来保护既得利益
- **创新热爱竞争，护城河憎恨它** - 金句

这段话完美解释了 Anthropic 焦虑的本质：

**他们不是在保护创新，而是在保护租金。**

当技术壁垒被突破，当"护城河"开始干涸，他们选择的不是加速创新，而是抱怨"被偷"。

这不是领先者的姿态，这是**落后者的恐慌**。

---

## 真正让 Anthropic 慌的是什么？

表面上是"蒸馏攻击"，实际上 Anthropic 怕的是另一件事：

**中国模型崛起得太快了。**

DeepSeek、月之暗面、MiniMax，这三家有个共同点——都在短时间内搞出了跟 Claude 差不多的能力，而且成本低得离谱。

DeepSeek V2 出来的时候，圈内人都惊了：这效果，这价格，怎么可能？

有评论直接戳中要害：

> "If they can distill Claude into smaller, cheaper, better models, shouldn't you guys be able to do the same thing but better?"
> 
> （如果别人能蒸馏出更小更便宜更好的模型，你们难道不应该能做到更好吗？）

**扎心了。**

如果 Anthropic 真的技术领先，为什么别人蒸馏一下就能追上？

**不是别人太强，是你不够强。**

真正强大的技术，不怕别人学。怕别人学的，说明也就那样。

---

## 为什么发在 X 上，而不是上法庭？

这是一个特别值得玩味的细节。

如果 Anthropic 真的有证据，为什么不起诉？为什么要在社交媒体上"喊冤"？

答案很简单：**上法庭需要证据，发推文只需要情绪。**

Anthropic 想要的是舆论，不是正义。他们想让整个行业觉得"中国公司在偷我们的技术"，从而建立起一道道德护城河。

但评论区不买账，因为大家都看明白了：

**你们当年爬全网数据的时候，问过创作者的意见吗？**

这就像一个人偷了全世界的书，开了个图书馆收费，然后抱怨别人抄了他的读书笔记。

**贼喊捉贼，不过如此。**

---

## 蒸馏到底是不是偷？

这里需要客观说一下。

模型蒸馏本身不是偷，是学术界公开的技术。Hinton 老爷子的论文摆在那，谁都可以学。

但"工业级蒸馏"确实是个灰色地带：
- 学术蒸馏：拿公开论文复现，没问题
- 商业蒸馏：海量调用竞品 API，用输出训练自己的模型，边界模糊

Anthropic 的指控之所以站不住脚，是因为他们自己的边界也很模糊。

**他们的 ToS 里明确禁止用 API 输出训练竞争模型了吗？** 如果没有，那这个指控就是无理取闹。

更何况，就算禁止了，执行起来也是难题。你怎么判断一个模型是不是蒸馏出来的？Kimi 说它是 Claude，就说明它是蒸馏的？那万一是幻觉呢？

**技术上很难举证，法律上更难追责。**

所以 Anthropic 选择了舆论战。但舆论战的前提是——你得占理。

而评论区已经给出了答案：**不占理。**

---

## 最后的最后

用马斯克和评论区的金句收尾：

> **"How dare they steal the stuff Anthropic stole from human coders??"**

> **"Innovation loves competition. Moats hate it."**

Anthropic 发这条推文，本想抢占道德高地，结果评论区的大型翻车现场说明——

**AI 行业的道德高地，谁都想抢，谁也站不稳。**

但历史不会同情落后者，只会奖励创新者。

与其发推文抱怨"被偷"，不如想想怎么把 Claude 做得更好。

**毕竟，如果你的模型真的够强，谁还愿意去蒸馏你呢？**

---

**P.S.** 评论区最毒舌的双关：
> "Rename Moonshot to Moonshine, it's illegally distilled"

Moonshine（私酿酒）和 Moonshot 押韵。笑死。

---

*本文基于 Anthropic 官方推文及评论区公开内容整理。数据截至 2026-02-24，评论区最高赞 290。抓取工具：x-tweet-fetcher + Camofox。个人观点，欢迎讨论。*
