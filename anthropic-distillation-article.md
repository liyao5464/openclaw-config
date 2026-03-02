# Anthropic 指控中国 AI "蒸馏攻击"，评论区却变成大型翻车现场

> "你们自己不也是靠偷全网数据起家的？"

---

## 一、凌晨的指控

今天凌晨，Anthropic 官方账号发布了一条措辞严厉的推文：

> "我们已经识别出针对我们模型的工业级蒸馏攻击，攻击方包括 DeepSeek、Moonshot AI 和 MiniMax。这些实验室创建了超过 24,000 个虚假账号，生成了超过 1,600 万次与 Claude 的对话，提取其能力来训练和改进他们自己的模型。"

**关键词解析：**
- **工业级蒸馏攻击**：这是 Anthropic 新造的词汇，暗示这不是学术研究，而是有组织的商业窃取
- **24,000 个虚假账号**：强调规模之大
- **1,600 万次对话**：强调投入之深
- **点名三家中国公司**：DeepSeek（深度求索）、Moonshot AI（月之暗面）、MiniMax

按常理，这种"正义声讨"应该获得支持。但点进评论区，画风却完全跑偏了。

---

## 二、评论区六大反噬派别

### 1. 双标揭露派（压倒性多数）

**最高赞评论（251赞）：**
> "HOW IS MODEL DISTILLATION STEALING 😭😭"

这条看似简单的评论，点出了核心矛盾：模型蒸馏在 AI 学术界是公开、常规的技术手段。OpenAI、Google、Meta 都曾发表论文介绍自己的蒸馏方法。Anthropic 把它定性为"攻击"，却没有解释清楚边界在哪里。

**更犀利的质疑：**
> "Anthropic 花 80 亿美元未经许可训练 Claude，DeepSeek 花 0 美元未经许可训练 Claude。Anthropic 生气是因为有人用更便宜的方式玩了他们自己的游戏。"

这句话获得大量认同，因为它揭示了一个尴尬的事实：Anthropic 自己也是靠爬取全网数据训练模型的，而这些数据的创作者并没有收到一分钱。

---

### 2. 付费客户派（逻辑暴击）

**121赞的高赞评论：**
> "so are they like paying customer here or whats up"
> （所以他们算是付费客户还是怎么回事？）

这个问题直击要害：如果这 24,000 个账号是正常注册、正常付费的 API 用户，那么 Anthropic 的指控就显得很微妙——用户付了钱，按照 ToS 使用 API，怎么突然就成了"欺诈"？

**进一步的追问：**
> "When you guys train your model by bombarding others for free of cost, it's fine. But if others are training by paying your model, it's illegal? Unethical?"
> （你们免费爬别人的数据训练模型就行，别人付费用你的模型训练就违法？就不道德？）

---

### 3. GitHub 旧账派（实名爆料）

最劲爆的来自一位自称前 GitHub 员工的评论：

> "We should have write a post like that when I was at GitHub, we had to ask you guys to stop putting our API at high capacity because you were Scrapping GitHub repos and it was against our ToS. You said sorry and continued doing so."
> 
> （我在 GitHub 工作的时候，我们不得不让你们停止过度使用我们的 API，因为你们违反 ToS 爬取 GitHub 仓库。你们道了歉，然后继续这么做。）

这条评论如果属实，那 Anthropic 的指控就变成了经典的"五十步笑百步"。

---

### 4. 隐私担忧派（GDPR 警告）

**来自欧盟用户的灵魂拷问（多赞）：**
> "By examining request metadata, we were able to trace these accounts to specific researchers at the lab. So… you're bragging you can de-anonymize users using metadata?"
> 
> （通过检查请求元数据，我们能够将这些账号追踪到实验室的具体研究人员。所以……你们在炫耀你们能用元数据去匿名化用户？）

这位用户连续追问：
1. 你们处理了哪些具体的"请求元数据"？
2. 根据 GDPR 第6条，这种处理的法律依据是什么？
3. 欧盟用户是否被告知（第13/14条）？
4. 这种元数据是否用于用户级别的归因/追踪？

这对 Anthropic 来说是个危险的信号——如果他们的追踪手段违反了 GDPR，可能面临巨额罚款。

---

### 5. 讽刺玩梗派（meme 大战）

**最毒舌的双关：**
> "Rename Moonshot to Moonshine, it's illegally distilled"
> （把 Moonshot 改名 Moonshine 吧，这是非法蒸馏的）

Moonshine（私酿酒）和 Moonshot 押韵，完美呼应了"蒸馏"这个梗。

**玩梗归玩梗，也有人认真科普：**
> "Distillation - 1. 向强大的 AI 问大量问题 2. 收集这些回答 3. 用这些回答训练自己的模型。通常这在研究中很常见，但在"攻击"中是大批量且未经许可进行的。"

**还有马斯克相关的：**
> "I have to agree with Musk here"（配图未显示，但暗示马斯克对此有表态）

**最萌的评论：**
> "Mom, the models are fighting"
> （妈妈，AI 模型们打起来了）

---

### 6. 国家安全派（少数派）

在一片嘲讽声中，也有严肃的声音：

> "lots of people thinking it's hypocrisy, but we should genuinely be concerned that China can just steal US frontier AI research this way, this is a matter of national security not just copyright"
> 
> （很多人认为是双标，但我们真的应该担心中国能用这种方式窃取美国前沿 AI 研究，这是国家安全问题，不只是版权）

这种观点代表了美国科技界的另一种担忧：技术竞争已经上升到国家战略层面。

---

## 三、技术争议：蒸馏到底算不算偷？

这场争论的核心是一个模糊地带：**模型蒸馏的伦理边界在哪里？**

**学术界共识：**
- 知识蒸馏（Knowledge Distillation）是 Geoffrey Hinton 等人在 2015 年提出的经典技术
- 目的是让小模型学习大模型的"软标签"，提高效率和性能
- 无数论文、开源项目都公开使用这项技术

**商业争议点：**
- 学术蒸馏 vs 工业级蒸馏：后者涉及海量 API 调用，成本巨大
- 公开 API 的使用权：用户协议是否禁止用输出训练竞争模型？
- "能力提取"的界定：如果只是学习风格 vs 复制核心能力，边界在哪里？

**Anthropic 的尴尬：**
他们自己的模型也是通过蒸馏技术优化的——从更大的模型中提取能力到更小的部署版本。所以他们反对的不是蒸馏本身，而是"未经许可的大规模蒸馏"。

但问题是：如果用户付了 API 钱，使用协议又没有明确禁止，这算什么"未经许可"？

---

## 四、中国 AI 公司的位置

被点名的三家公司，代表了不同的技术路线：

**DeepSeek（深度求索）**：
- 以极低成本训练出高性能模型闻名
- DeepSeek-V2 的性价比震惊业界
- 被质疑"成本优势"来源不纯

**Moonshot AI（月之暗面）**：
- Kimi K2.5 在长文本领域表现突出
- 被评论调侃"问 Kimi 它是谁，它会告诉你它是 Claude"

**MiniMax**：
- 国内大模型"六小龙"之一
- 语音和多模态能力较强

这三家的共同点：都在短时间内实现了与 Claude 相媲美的能力，而 Anthropic 认为这不是独立研发的结果。

---

## 五、更深层的行业矛盾

这场风波暴露了几个结构性矛盾：

**1. 开源精神 vs 商业护城河**
- AI 行业建立在开源论文、开源代码之上
- 但当公司融了数十亿美元，就需要建立"护城河"
- "蒸馏攻击"这个概念的提出，本质上是在重新定义什么是"合法学习"、什么是"窃取"

**2. 数据殖民主义 vs 数据主权**
- 欧美 AI 公司爬取全球互联网数据训练模型，被称为"创新"
- 中国公司用 API 输出训练模型，被称为"攻击"
- 这种不对称的叙事，反映了 AI 时代的新殖民主义

**3. 技术领先者的焦虑**
- Anthropic 曾经以"AI 安全"和" Constitutional AI"为差异化卖点
- 但现在发现，技术壁垒比想象中脆弱
- "蒸馏攻击"的指控，某种程度上是技术焦虑的外化

---

## 六、关键金句汇总（中英文对照）

| 类型 | 金句 | 点赞数 |
|------|------|--------|
| 最毒舌 | "$80亿 vs $0：Anthropic 生气是因为有人用更便宜的方式玩了他们自己的游戏" | 高赞 |
| 最讽刺 | "把 Moonshot 改名 Moonshine，非法蒸馏的" | 高赞 |
| 最技术 | "问 Kimi K2.5 它是谁，温度调高点，它会告诉你它是 Claude" | 44赞 |
| 最扎心 | "妈妈，AI 模型们打起来了" | 高赞 |
| 最直接 | "HOW IS MODEL DISTILLATION STEALING" | 251赞 |
| 最疑问 | "所以他们算是付费客户还是怎么回事？" | 121赞 |
| 最爆料 | "我在 GitHub 的时候，你们违反 ToS 爬数据，道歉了继续爬" | 实名 |
| 最安全 | "你们能用元数据追踪用户？GDPR 怎么说？" | 多赞 |
| 最专业 | "24,000 个付费客户用产品让你们不满... 你们不想让人用的东西怎么规模化？" | 高赞 |
| 最玩梗 | "如果是真的，为什么发在 X 上而不是上法庭？" | 高赞 |

---

## 七、结语

Anthropic 发布这条推文，本意可能是想抢占道德高地，向业界警示"蒸馏攻击"的风险。但评论区的大型翻车现场说明，**公众并不买账这种叙事**。

原因很清晰：
1. ** credibility problem**：指控者自己的"数据原罪"还没洗清
2. ** definition problem**："蒸馏攻击"的边界模糊不清
3. ** fairness problem**：双重标准的叙事难以服人

更有趣的是，这条推文本身成了一个绝佳的社会实验——它展示了全球 AI 社区对"数据所有权"、"模型训练伦理"、"中美 AI 竞争"等议题的真实态度。

**最后，用一条评论总结这场风波：**

> "It sucks to have your art scraped and stolen by an AI company doesn't it…"
> （被 AI 公司抓取和窃取作品的感觉很糟糕，对吧……）

这条评论获得了大量点赞。它的讽刺之处在于：这正是无数艺术家、作家、程序员对 Anthropic 等 AI 公司说过的话。

当 AI 公司成为被"蒸馏"的一方，他们终于体会到了被爬取数据者的感受。只不过，这次轮到他们自己来解释：**为什么同样是提取数据，他们做的就是"创新"，别人做的就是"攻击"？**

这个问题，Anthropic 还没有给出令人信服的答案。

---

*本文基于 Anthropic 官方推文及评论区公开内容整理，抓取工具：x-tweet-fetcher + Camofox*
