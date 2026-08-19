# 总体判断

基于你贴出的设计摘要，我的结论是：

```
DEVELOPMENT_GRAMMAR_V0_REVIEW = REVISE
ARCHITECTURE_DIRECTION = STRONGLY_ACCEPT
READY_FOR_REAL_REPOSITORY_USE = AFTER_SMALL_BUT_IMPORTANT_AMENDMENTS
```

这套框架的**大方向是对的，而且比单纯做“Spec 模板 + CI 门禁”高一个层次**。它真正建立的是：

```
仓库如何表达事实
→ 如何从事实形成判断
→ 如何做决定
→ 如何把决定变成实现契约
→ 如何判断代码是否兑现契约
```

尤其以下四点非常好：

1. `.agents/`只保存稳定 Grammar、Protocol、Skill，不成为第四套项目知识库；
2. governing Spec 固定放在 `docs/specs/`，路径稳定，生命周期不靠移动目录表达；
3. accepted Spec 与 implemented state 被明确拆开；
4. Spec 必须先进入 implementation base，避免“代码做完了再补一份解释代码的 Spec”。

它完全适合 `dsh-agent-core` 这种大量由 Agent 持续开发、跨多轮对话、容易出现文档 authority 冲突的仓库。

但当前设计里仍有几处**类型系统自身不一致**。不修的话，运行一段时间后会出现“看起来治理很严格，实际上状态仍说不清”的问题。

---

# 一、六个原语的方向正确，但不应被描述成六种完全同类的东西

当前六个原语：

```
Goal
State
Observation
Claim
Decision
Contract
```

是合理的，但它们实际上分属两个不同世界。

## 认识世界的原语

```
Observation
Claim
State
```

- `Observation`：在特定时间、特定 commit、特定环境中观察到什么；
- `Claim`：根据 Observation 得出的可争论判断；
- `State`：在某个时点，我们接受为“当前状态”的一组 Claim 的汇总。

## 改变世界的原语

```
Goal
Decision
Contract
```

- `Goal`：希望达到什么结果；
- `Decision`：在多个方案中选择哪一个；
- `Contract`：选择之后，系统必须满足什么。

建议在 Grammar 里明确加上这两个分类，否则 Agent 很容易把 `State` 当成与 Observation 同等的原始事实，或者把 `Goal`误当成已经产生约束力的 Contract。

推荐关系图：

```
Observation
  → supports / refutes Claim

Claim
  → contributes to State
  → informs Decision

Goal + State + Claims
  → Decision

Decision
  → creates / amends / supersedes Contract

Implementation Evidence
  → verifies / refutes Contract

State
  → 是带时间坐标的当前投影
  → 不是永恒事实
```

最重要的一句应该是：

```
State is a time-indexed projection, not raw truth.
```

---

# 二、`State`不能只定义为“当前代码实际上是什么”

这是当前原语设计中最容易产生歧义的地方。

“当前代码实际上是什么”至少可能指：

```
main 分支源码是什么
某个 PR 分支源码是什么
本机部署运行的是什么
生产机器部署的是什么
数据库中的真实状态是什么
用户真正能访问到的是什么
```

这些状态可能完全不同。

所以任何重要 State 都必须带坐标，至少包括：

```
STATE_SUBJECT
AS_OF_COMMIT
ENVIRONMENT
OBSERVED_AT
BASIS / PROVENANCE
```

例如：

```
State:
  subject: production auth contract mode
  as_of_commit: 93f9acf
  environment: local production runtime on host X
  observed_at: 2026-08-18T...
  value: v1
  basis:
    - runtime banner
    - audit log event counts
```

而不能只写：

```
Current mode = v1
```

建议将原规则从：

```
State = 当前代码实际上是什么
```

改成：

```
State = 对某个明确 subject 在明确 commit / environment / time 下的当前状态判断，
        由 Observation 支撑，可随新 evidence 更新。
```

---

# 三、当前 Spec 生命周期缺少 `rejected`

你现在允许的生命周期是：

```
proposed
accepted
superseded
```

这里有一个明显缺口：

> 一个经过真实调查、最终被否决的 proposed Spec 应该放在哪里？

如果不允许 `rejected`，最终只能：

- 删除它，丢失为什么没选；
- 永远留在 `proposed`，让人误以为还在讨论；
- 标成 `superseded`，但它实际上从未成为 authority。

这三种都不准确。

推荐生命周期：

```
proposed
accepted
rejected
superseded
```

转换关系：

```
proposed → accepted
proposed → rejected
accepted → superseded
```

`rejected` 必须要求：

```
Rejected because
What would reopen this decision
Evidence considered
```

这不会重新引入 `rejected/`目录，也不会混淆 implementation state。它只是一个必要的 Spec 决策结果。

这是我认为接受框架前的**必修项**。

---

# 四、Implementation Conformance 枚举仍然混合了三种不同概念

当前设计：

```
UNKNOWN
NOT_STARTED
PARTIAL
VERIFIED
DRIFTED
```

看起来是一套状态，但其实混合了：

| 值实际表达的维度      |            |
| ------------- | ---------- |
| `NOT_STARTED` | 实施进度       |
| `PARTIAL`     | 实施进度或证据完整度 |
| `VERIFIED`    | 契约一致性      |
| `DRIFTED`     | 契约一致性      |
| `UNKNOWN`     | 我们是否知道     |

这违反了框架自己强调的“不同类型不能混写”。

应拆成至少两个维度：

```
IMPLEMENTATION_STATE =
  NOT_STARTED
  IN_PROGRESS
  COMPLETE

CONFORMANCE =
  UNKNOWN
  VERIFIED
  DRIFTED
```

必要时再单独表达验证充分度：

```
VERIFICATION_STATE =
  NOT_RUN
  PARTIAL
  SUFFICIENT
```

但 V0 可以先不增加第三维，只保留前两个。

于是以下情况才能被准确表达：

```
Spec lifecycle: accepted
Implementation state: COMPLETE
Conformance: DRIFTED
```

或者：

```
Spec lifecycle: accepted
Implementation state: IN_PROGRESS
Conformance: UNKNOWN
```

而不是让 `PARTIAL`同时承担“做了一半”和“验证了一半”两种含义。

这是第二个必须修正的类型问题。

---

# 五、`Test ≠ Evidence`这句话需要改得更精确

原方向是对的，但现在的表述容易让人误解成“测试不是证据”。

更准确的规则应该是：

```
Test Definition ≠ Evidence
Executed Test Result = Evidence
```

或者中文：

```
测试代码本身不是通过证明；
在明确 commit、环境和输入下执行所得的结果，才是 Evidence。
```

例如：

```
packages/router/test/foo.test.js
```

只是一个验证机制。

只有以下记录才是 Evidence：

```
commit = abc123
command = npm test
environment = Node 25.6.1 / macOS
result = 440 passed, 0 failed, 1 skipped
observed_at = ...
```

同理：

```
日志文件 ≠ Evidence
日志中与某个 Claim 建立了明确 provenance 关系的片段 = Evidence
```

你原来“Evidence 是关系而不是材料本身”的方向很好，建议在这里落到这种可执行定义上。

---

# 六、Spec 的 authority 变更规则需要比 REUSE / AMEND / SUPERSEDE / NEW 再精确一步

这四种 Preflight 结果很好：

```
REUSE
AMEND
SUPERSEDE
NEW
```

但还缺少“如何完成 authority 交接”。

## AMEND

建议冻结：

```
已有 owner Spec
→ 在独立 docs-only PR 中修改
→ amendment 期间 PR 分支上 status 可为 proposed
→ 复审通过后再改回 accepted
→ 最终以 accepted 状态 merge
```

不能在 implementation PR 里边改 Contract 边写代码。

## SUPERSEDE

必须保证原子交接：

```
new Spec → accepted
old Spec → superseded
old Spec.replaced_by → new Spec ID
new Spec.supersedes → old Spec ID
```

最好在同一个 docs-only PR 中完成，避免出现：

```
新 Spec accepted
旧 Spec 仍 accepted
```

导致两套相反 authority 同时存在。你刚才在 `dsh-agent-core` PR #11 遇到的就是这种问题。

## 部分 supersession

还要注意一个 Spec 可能只有一个 Contract 被替换，而不是整份 Spec 被废弃。因此 Contract 必须有稳定 ID：

```
C-001
C-002
C-003
```

允许表达：

```
amends:
  - OLD_SPEC#C-003
```

V0 不一定要立刻实现复杂 contract graph，但至少要冻结：

```
Contract ID 一旦 accepted，永不重编号、永不复用。
```

否则 COMPLIANCE 中的：

```
Contract ID → implementation → evidence
```

会随着文档插入章节而失效。

---

# 七、Implementation 必须固定自己审的是哪个 Spec revision

稳定路径意味着 accepted Spec 以后可能被 amendment。

假设：

```
Implementation PR 开始时：
SPEC_A.md @ commit A

三天后：
SPEC_A.md 被 amendment @ commit B
```

后续仅写“governing Spec = SPEC\_A”已经不够，必须知道实现是按哪个版本做的。

建议 Implementation PR 固定记录：

```
GOVERNING_SPEC = SPEC_A
GOVERNING_SPEC_BASE_COMMIT = <implementation PR merge-base>
GOVERNING_SPEC_BLOB_SHA = optional
```

最少要有：

```
SPEC_PRESENT_IN_BASE = YES
SPEC_STATUS_IN_BASE = accepted
BASE_COMMIT = ...
```

这使“accepted 且存在于 base branch”从一句原则变成可审计事实。

同时要支持多个 authority：

```
PRIMARY_GOVERNING_SPEC
RELATED_ACCEPTED_SPECS
RELATED_DECISIONS
```

因为真实改动经常同时受一个主 Spec 和几个长期 invariant 约束。

---

# 八、独立 Review 不能等于自动接受

现在 Skill 的 REVIEW 输出：

```
SPEC_REVIEW = ACCEPT | REVISE
READY_TO_MARK_ACCEPTED = YES | NO
```

这是合理的，但必须补一句：

```
Review recommendation ≠ acceptance authority
```

独立 Agent 可以给出：

```
READY_TO_MARK_ACCEPTED = YES
```

但不能因此自己直接成为最终决策者。

建议冻结：

```
REVIEWER = independent semantic reviewer
ACCEPTANCE_ACTOR = repository owner / authorized maintainer
```

接受动作可以很轻：

```
review PASS
→ authorized actor 将 status proposed 改为 accepted
→ merge docs-only PR
```

不必增加复杂审批流，也不必增加第五个 Skill mode，但必须说清楚谁能完成状态翻转，避免 Author Agent 自写、自审、自接受。

---

# 九、需要正式支持 Program Spec，否则宽泛 Program 很容易被误用为代码授权

你现在的实际开发方式已经出现了两类 Spec：

```
Program Spec
Implementation / Change Spec
```

例如一个 Program Spec可能只负责：

- 冻结总体问题；
- 冻结实施顺序；
- 拆 child Specs；
- 处理 authority 关系。

它不应该直接授权代码。

建议最小增加：

```
spec_kind: program | implementation
```

或者正文中强制声明：

```
IMPLEMENTATION_AUTHORITY = NONE | CONTRACTS
```

规则：

```
Program Spec accepted
≠ 其全部 child implementation 已获授权

只有 accepted implementation Spec
→ 才能授权对应代码修改
```

这能避免未来某个 Agent拿着一份范围极大的 Program Spec，说“总方向已经 accepted，所以我可以一次把五项都实现”。

---

# 十、COMPLIANCE 的结果必须有持久落点，不能只存在于聊天中

固定输出格式很好：

```
CONFORMANCE = VERIFIED | PARTIAL | DRIFTED
IMPLEMENTATION_READY_TO_MERGE = YES | NO
```

但必须说明结果保存在哪里。

推荐最轻方案：

## 普通 Implementation PR

PR 描述中必须包含：

```
## Spec Conformance

| Contract | Implementation | Test / Evidence | Result |
|---|---|---|---|
| C-001 | ... | ... | VERIFIED |
```

GitHub PR 本身就是持久审查记录。

## 跨环境或生产验收

如果 evidence 超出单个 PR，例如：

- 生产 canary；
- 真实 auth-service；
- 真实飞书；
- 多次重启；
- 数据迁移；

再落入：

```
docs/reports/<IMPLEMENTATION_OR_ACCEPTANCE_REPORT>.md
```

不建议每个小 PR 都新建报告，也不建议把 conformance 结果写回 Spec frontmatter。Spec 是 Contract authority，不应承担不断变化的部署状态。

---

# 十一、必须定义“机械性改动”，否则 Gate 会被不断绕过

“非机械性开发必须有 accepted Spec”本身没问题，真正危险的是大家开始争论：

```
这个只是小修
这个只是重构
这个只是测试
这个只是依赖升级
```

建议冻结默认规则：

```
UNCERTAIN = NON_MECHANICAL
```

明显可以视为机械性的只包括：

- 纯拼写修正；
- 不改变解释结果的格式化；
- 已有 Contract 明确要求的确定性生成物刷新；
- 路径移动且有机器证明语义不变。

以下默认不是机械改动：

- dependency upgrade；
- schema change；
- 权限变化；
- retry/timeout变化；
- test expectation变化；
- public API rename；
- “仅重构”但改变模块边界；
- 删除 seemingly unused code。

生产紧急情况也不需要破坏 Spec-before-code：

```
操作性 containment
如停止服务、回滚、关闭 flag
→ 可以立即执行并保留 evidence

永久代码修复
→ 仍然需要 accepted Spec
```

这样既不会让治理阻碍止血，也不会允许“紧急”为理由永久绕过 authority。

---

# 十二、1652 行并非一定太长，但必须防止规则重复

最大使用风险不是内容错误，而是：

> Agent 每次进入仓库都要读一千多行，然后实际只记住其中十分之一。

建议保证三层只有一个 owner：

| 文件唯一职责                 |                                         |
| ---------------------- | --------------------------------------- |
| `AGENTS.md`            | 最薄入口和必读顺序                               |
| `.agents/README.md`    | Grammar、生命周期、authority 原则               |
| `SKILL.md`             | 如何执行 PREFLIGHT/AUTHOR/REVIEW/COMPLIANCE |
| `docs/specs/README.md` | Spec 文件格式和 frontmatter syntax           |

同一规则不要四处完整复制。

`.agents/README.md`顶部最好有一个一屏能读完的 **Minimum Operating Loop**：

```
1. 找 governing authority
2. 输出 REUSE / AMEND / SUPERSEDE / NEW
3. 无 accepted Spec in base → 不改代码
4. Spec PR 与 Implementation PR 分离
5. 实现后做 Contract-by-Contract Compliance
6. 发现 drift → 报告，不改 Spec 粉饰代码
```

详细哲学、案例和反例可以继续放在后面。

---

# 建议接受前必须修改的内容

我会把它压缩成下面七项：

```
REQUIRED_FIXES = [
  "Spec lifecycle 增加 rejected，并要求 Rejected because / What would reopen。",
  "将 Implementation State 与 Conformance 拆成两个维度，不能继续混用 NOT_STARTED/PARTIAL/VERIFIED/DRIFTED。",
  "将 State 定义为带 commit/environment/time/provenance 的 time-indexed projection，而不是无坐标的“实际状态”。",
  "冻结 AMEND / SUPERSEDE 的 authority 交接规则，supersession 必须有双向 backlink，并避免两份冲突 accepted authority 共存。",
  "Contract 使用稳定 ID；accepted 后不得重编号或复用，Acceptance/Compliance 必须引用 Contract ID。",
  "明确独立 Review 只是接受建议，status: accepted 只能由 repository owner / authorized maintainer 完成。",
  "Implementation PR 必须记录 governing Spec 的 base commit/revision，Compliance 结果必须持久化在 PR 或必要的 report 中。"
]
```

建议一并修正但不构成 blocker：

```
Test Definition ≠ Evidence
Executed Test Result = Evidence

增加 Program Spec 与 Implementation Spec 的区别

定义 mechanical change 的窄范围与 uncertain 默认 non-mechanical
```

---

# 是否适合用于 `dsh-agent-core`

**适合，而且非常适合。**

这个仓库最容易发生的问题恰好是该框架针对的问题：

```
旧 Architecture 说一件事
新 Spec 说另一件事
实现报告又说已经 PASS
生产现场却是第四种状态
```

这套 Grammar 能把它们拆开：

```
Architecture / Decision
→ 长期方向

Spec / Contract
→ 这次允许改变什么

Code
→ 实际实现

Runtime Observation
→ 现场发生了什么

Compliance
→ 实现是否满足 Contract

Drift
→ 哪一层和哪一层不一致
```

但落地时应采用 **forward-only**，不要一上来迁移所有历史文档：

```
从下一个 non-mechanical change 开始严格执行
旧 artifact 只有在成为 governing authority、被引用或发生冲突时才治理
不批量重写历史
不建立数据库
不建立中央 Spec Registry
不建立复杂审批平台
```

运行两个到三个真实 Spec 周期后，再根据实际痛点实现 deterministic verifier。不要在还没使用过框架前，就把所有可能规则全部写进 CI。

# 最终评价

这不是一套“文档规范”，而是一套基本成立的**仓库级开发类型系统**。

它最有价值的部分是：

```
Spec lifecycle
≠ Implementation progress
≠ Runtime state
≠ Conformance result
```

但当前恰恰还需要把这个原则贯彻到底：补上 `rejected`，拆开 Implementation State 与 Conformance，为 State 增加时间坐标，并把 amendment/supersession 的 authority 交接真正冻结。

完成这些后，我会给出：

```
DEVELOPMENT_GRAMMAR_AND_SPEC_GOVERNANCE_V0 = ACCEPT
SUITABLE_FOR_DSH_AGENT_CORE = YES
SPEC_GOVERNANCE_DIRECTION = KEEP
DETERMINISTIC_GATE = DEFER_UNTIL_REAL_USAGE_EVIDENCE
```