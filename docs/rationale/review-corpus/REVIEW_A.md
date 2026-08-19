# 审查结论

```
DEVELOPMENT_GRAMMAR_AND_SPEC_GOVERNANCE_V0_REVIEW = REVISE
DIRECTION = KEEP
FRAMEWORK_REWRITE_REQUIRED = NO
READY_TO_MARK_ACCEPTED = NO
BLOCKERS = 4
```

我审的是 **PR #4 当前 head** **`a22dd9fc`**；PR 仍是 Draft、未合并，base 仍为 `main @ 502cfca5`，当前 `main` 也没有继续移动。变更范围确实只有这 4 个治理文件，没有 Forum 产品代码。

整体方向很好，已经不是“再讨论一下概念”的阶段，而是**接近可以成为仓库治理基础**。真正的问题只有少数几个，但都在 authority 和可追溯性核心上，最好在第一份 `AGENT_FORUM_CORE_INVARIANTS_V1` 出现前修掉。

---

## 一、这个框架最正确的地方

### 1. Spec 生命周期与代码一致性拆开，是整个设计最重要的决定

```
Spec: accepted
Conformance: drifted
```

这是完全正确的。

它避免了非常常见的坏做法：

```
代码已经这么实现
→ 所以修改 Spec
→ 让 Spec 看起来重新“正确”
```

你现在冻结的是：

```
accepted Spec = 规范 authority
code = 当前 implementation state
二者冲突 = drift
```

这个原则应当保留，不要在修改时动摇。PR 也确实没有用 `implemented` 作为 Spec 生命周期，而是单独定义一致性状态。

### 2. governing Spec 必须先进入 implementation PR 的 base，设计非常强

这比“实现 PR 同时带一份设计说明”强很多。

它真正阻止的是：

```
先写代码
→ 代码反向塑造设计
→ 最后补一份解释现状的 Spec
```

根 `AGENTS.md` 入口也足够薄，只保留不可绕过的规则，没有复制整套语法。

### 3. `REUSE / AMEND / SUPERSEDE / NEW` 是非常有价值的开工分类

这会迫使 Agent 先回答：

> 这是已经被治理的工作，还是在修旧规范，还是改变旧决定，还是一个真正的新问题？

它能明显减少重复 Spec 和“偷偷改方向”的情况。

### 4. `Contract → implementation → evidence` 是正确的合规单位

不是：

```
PR 看起来合理
测试全绿
代码写得漂亮
```

而是：

```
每一个 Contract
→ 由哪些实现满足
→ 由哪些测试或运行事实验证
→ 是否仍有覆盖缺口
```

Skill 对真实入口、绕过路径、身份、事务失败、删除状态、重试等也有明确要求，已经明显超过普通的“设计文档模板”。

### 5. 没有用 Skill 冒充机器门禁，这一点很诚实

PR 明确承认：

```
SPEC_VERIFIER_IMPLEMENTED = NO
```

也把语义判断与 deterministic parser 分开。这个阶段先跑一个真实 Pilot，再自动化格式，顺序是合理的。

---

# 二、接受前需要修掉的 4 个问题

## BLOCKER 1：Authority 层级与 partial supersession 没有真正闭合

现在同时存在三条规则：

1. `docs/product/agent-forum-product-direction-v1.md` 是冻结的高层产品边界；
2. `docs/specs/` 中的 accepted Spec 可以细化，甚至“显式 supersede”产品方向；
3. partial supersession 时，不把旧 Spec 整体标为 superseded，而是保留两份 authority，并在正文中说明各自范围。

问题是，当前机器可读模型只有：

```
spec_id:
status:
scope:
supersedes:
superseded_by:
```

它只足以表达**整份 Spec 被另一份 Spec 取代**，表达不了：

```
新 Spec 只覆盖旧 Spec 的 CTR-A-003
其余 Contract 仍由旧 Spec 治理
```

更表达不了：

```
普通产品 Spec 是否有权修改更高层的 Product Direction
```

而且当前 Product Direction 自己没有 `authority_id`、正式生命周期或可被 `supersedes` 引用的 Spec ID，只写着“产品边界冻结稿，供评审使用”。

这会产生一个危险状态：

```
Spec A: accepted, scope = svc-forum
Spec B: accepted, scope = svc-forum
两者部分冲突
两者都没有 superseded
```

此时 Agent 和未来 verifier 都无法确定谁优先。

### V0 最简单的修法

不要现在引入复杂的 per-Contract authority graph，先冻结：

```
AUTHORITY_PRECEDENCE =
Product Direction
> Governing Product / Architecture Spec
> Code / Tests / Runtime

LOWER_LEVEL_SPEC_MAY_REFINE_PARENT = YES
LOWER_LEVEL_SPEC_MAY_SILENTLY_OVERRIDE_PARENT = NO

PARTIAL_SUPERSESSION_V0 = FORBIDDEN
```

同时二选一：

**推荐方案：**

给 Product Direction 增加稳定 authority ID 和正式状态，例如：

```
---
authority_id: AGENT_FORUM_PRODUCT_DIRECTION_V1
status: accepted
authority_kind: product_direction
---
```

每份下游 Spec 显式写：

```
governed_by:
  - AGENT_FORUM_PRODUCT_DIRECTION_V1
```

只有新的 Product Direction authority 才能 supersede 旧 Product Direction；普通实现级 Spec只能细化，不能改变它。

另外，下一份 Core Invariants 会触及身份和权限，建议允许记录跨仓库依赖：

```
external_authorities:
  - repo: mayf3/auth-service
    spec_id: ...
    commit: ...
```

Forum Spec 可以依赖 auth-service Contract，但不能替 auth-service 决定它自己的行为。

---

## BLOCKER 2：`AMEND` 可能让 accepted Contract 在同一个 ID 下改变含义

目前 `AMEND` 被定义为：

```
同一个 Goal、authority 和核心 Decision，
但可以补齐 Contract、修复歧义或改变仍属于同一决策的边界。
```

这意味着一份已经 accepted 的 Spec 可以继续原地修改，而且仍使用相同：

```
spec_id
Contract ID
稳定文件路径
```

问题不在于 Git 没有历史；Git 有历史。

问题在于 Skill 和未来实施报告主要引用的是：

```
GOVERNING_SPEC = <spec_id>
CTR-REVIEW-001
```

如果 `CTR-REVIEW-001` 在两个月后改变了语义，仅引用 ID 已经无法知道它指的是哪个 authority revision。

更严重的是，当前接受流程是：

```
Reviewer 审 proposed head
→ Author 把 status 改成 accepted
→ 再 merge
```

虽然 Skill 写了“重新检查”，但 REVIEW 输出没有强制记录：

```
REVIEWED_SPEC_COMMIT
FINAL_ACCEPTED_HEAD
SPEC_BODY_HASH
```

因此 review 结论没有被严格绑定到最终被 merge 的内容。

### 推荐的 V0 规则

```
ACCEPTED_NORMATIVE_TEXT_IMMUTABLE = YES

AMEND_AFTER_ACCEPTANCE =
EDITORIAL_OR_ADDITIVE_ONLY

EXISTING_DECISION_OR_CONTRACT_MEANING_CHANGE =
SUPERSEDE
```

也就是说：

- proposed 阶段可以自由 amend；
- accepted 后，拼写、链接、纯解释性补充可以原地改；
- 增加不影响既有 Contract 的补充内容可以经独立 review 后 amend；
- 删除、收缩、扩大、反转既有 Decision 或 Contract，必须创建新的 Spec ID 并 supersede；
- 旧 Contract ID 永远不能被重新赋予另一种含义。

接受流程还应强制输出：

```
REVIEWED_BASE_COMMIT = ...
REVIEWED_SPEC_COMMIT = ...
REVIEWER_ID = ...
FINAL_ACCEPTED_HEAD = ...
SEMANTIC_DELTA_AFTER_REVIEW = NONE
```

如果从 `REVIEWED_SPEC_COMMIT` 到最终 accepted head 不只是 `status` 变化，则必须重新进行独立 REVIEW。

另一种方案是允许原地修订，但需要引入 `revision`、Contract tombstone 和精确 revision mapping。对 V0 来说复杂度明显更高，不如先采用 accepted normative content 不可变。

---

## BLOCKER 3：Conformance 不是一个脱离版本的状态，而是一个带版本的关系

当前定义：

```
UNKNOWN
NOT_STARTED
PARTIAL
VERIFIED
DRIFTED
```

方向正确，但还缺少最重要的一句话：

> `VERIFIED` 不是某份 Spec 的永久属性，而是某个 Spec 版本、某个代码版本、某个环境之间的一次评估结果。

否则今天：

```
CONFORMANCE = VERIFIED
```

明天代码变了、Spec amend 了、生产配置变了，这个 `VERIFIED` 到底还算不算有效，没有正式语义。

### 应冻结为

```
Conformance Record =
(
  spec_id,
  spec_commit_or_blob,
  implementation_commit,
  environment,
  evaluated_at,
  result,
  evidence
)
```

例如：

```
SPEC_ID = AGENT_FORUM_CORE_INVARIANTS_V1
SPEC_COMMIT = abc123
IMPLEMENTATION_COMMIT = def456
ENVIRONMENT = test | staging | production
EVALUATED_AT = 2026-08-18T...
CONFORMANCE = VERIFIED
EVIDENCE = ...
```

并明确：

```
任何一个被绑定的 Spec、代码或环境发生变化
→ 旧记录仍是历史证据
→ 但不自动代表新版本 VERIFIED
```

V0 不需要现在建设数据库，也不一定需要新增 conformance 目录。先让 Compliance PR 报告成为 point-in-time record 即可；以后数据库只负责索引和查询这些记录。

否则“Spec lifecycle 与 conformance 分离”只是状态名分离，还没有成为可计算的关系模型。

---

## BLOCKER 4：`State` 与 `Observation` 之间仍有语义泄漏

当前定义中：

```
State = 当前系统客观上是什么
Observation = 实际看到、读取、复现或测量到了什么
```

两者很容易重叠。

Agent 可以在 `Current State` 中直接写：

```
当前系统保证 X
```

却不写 Observation 或 provenance，从而绕过你对 Observation 的证据要求。

同时正文骨架使用了类似：

```
VERIFIED CLAIM
INFERRED CLAIM
UNVERIFIED ASSUMPTION
```

“VERIFIED CLAIM”又会弱化：

```
Observation ≠ Claim
```

因为 Claim 本来就是解释性、可被新证据削弱的命题。更准确的说法应是“得到强证据支持”，而不是“已经成为 Observation”。

### 应补充两条冻结规则

```
State =
在固定 commit / environment 上，
由 Observations 和必要 Claims 构成的版本化系统快照。

State 本身没有独立证据权威。
每个 load-bearing State statement
必须引用 provenance、OBS ID 或 CLM ID。
```

Claim 的证据状态改成：

```
SUPPORTED CLAIM
INFERRED CLAIM
OPEN ASSUMPTION
```

不要使用：

```
VERIFIED CLAIM
```

这样关系才完整：

```
Observation
→ supports / contradicts
→ Claim
→ contributes to
→ Current State model
```

---

# 三、不阻塞方向，但建议一起优化

## 1. 明确 V0 只是人工 Policy Gate，不是已经存在的 Merge Gate

当前 `main` 分支仍是：

```
protected = false
required checks = off
```

所以即使仓库里存在工作流，当前 GitHub 设置也没有形成不可绕过的分支保护。

PR 已经诚实声明 verifier 尚未实现，因此只需把措辞再收紧：

```
ENFORCEMENT_LEVEL_V0 = MANUAL_POLICY
DETERMINISTIC_FORMAT_GATE = NOT_IMPLEMENTED
BASE_BRANCH_MERGE_GATE = NOT_IMPLEMENTED
```

把 `.agents/README.md` 中的 “Spec-first Merge Gate” 暂时改成：

```
Spec-first Policy Gate
```

等 verifier、PR metadata validator 和 branch protection 都实际接通后，再叫不可绕过的 Merge Gate。

## 2. 常驻治理内容过长，而且 README 与 Skill 重复较多

当前：

```
.agents/README.md = 1068 行
SKILL.md = 508 行
```

而 `AGENTS.md` 要求 Agent 先读 README，再使用 Skill。也就是说一个普通非机械性任务，在读具体 Spec 和代码前，已经要加载约 1500 行治理指令。

建议保持内容，但重新分层：

```
.agents/README.md
只留 normative constitution

.agents/skills/spec-governance/SKILL.md
只留执行步骤、检查表和输出格式

docs/governance/DEVELOPMENT_GRAMMAR_V0_RATIONALE.md
设计来源、被拒绝方案、Pilot 顺序、成功标准、未来方向
```

尤其 `.agents/README.md` 的设计来源、完整 alternatives、Pilot、V0 成功标准和“不做什么”，不必成为每次任务的常驻上下文。

## 3. Mechanical exemption 不能只由 PR 作者自己声明

目前：

```
SPEC_REQUIRED = NO
MECHANICAL_REASON = ...
```

是必要的，但不充分。否则最容易绕过的方式就是把行为变化说成“小重构”。

建议增加：

```
MECHANICAL_EXEMPTION_REVIEWED_BY = <independent reviewer>
MECHANICAL_EXEMPTION_RESULT = ACCEPT | REJECT
```

以后机器只能检查字段存在，真正是否 mechanical 仍由 Reviewer 判断。

## 4. 每个 Contract 都应被 Acceptance 覆盖，而不仅是 Acceptance 引用了有效 Contract

当前 syntax pass 检查：

```
每个 Acceptance 引用的 Contract ID 必须存在
```

还应反向检查：

```
每个 active Contract
至少被一个 Acceptance item 覆盖
或明确标记为需要 runtime/manual evidence 并说明原因
```

否则可能出现 20 个 Contract，只有 8 个真正进入验收计划。

## 5. 需要给“调查后决定不改”留一个轻量持久化出口

当前被拒绝的 proposed Spec 通常不进 main，理由尽量吸收到最终 accepted Spec。这个原则对于存在最终 Spec 的情况成立。

但如果调查结论是：

```
REUSE
NO_CHANGE
CLAIM_REJECTED
IMPLEMENTATION_NOT_WORTH_DOING
```

就不一定有一份新 Spec 来承载长期证据，最后只剩聊天和关闭的 PR。

V0 不必新增复杂目录，但应明确：

```
无新 Spec 的重要调查结论
必须保存在可检索的 GitHub Issue / Investigation PR 中，
并由现有 Spec、产品文档或索引保存稳定引用。
```

否则“被拒绝方案不再被重复提出”这一成功标准无法稳定实现。

## 6. 增加极窄的紧急处置规则

生产故障或安全事件不应等待完整 Spec 周期才能止血。

可以冻结：

```
EMERGENCY_REMEDIATION =
rollback | disable | containment only

NEW_DURABLE_BEHAVIOR_ALLOWED = NO
OWNER_APPROVAL_REQUIRED = YES
INCIDENT_REFERENCE_REQUIRED = YES
POST_INCIDENT_SPEC_RECONCILIATION_REQUIRED = YES
```

这不是给普通开发开后门，而是避免治理系统阻止回滚和安全隔离。

---

# 四、最终建议

这个 PR **不应该推翻，也不应重新设计目录**。以下内容应原样保留：

```
AGENTS.md 作为最薄入口
.agents/ 保存 Grammar 与 Skills
docs/specs/ 保存 governing Specs
proposed / accepted / superseded
Spec lifecycle 与 conformance 分离
REUSE / AMEND / SUPERSEDE / NEW
Spec 与 Implementation 不在同一 PR
accepted Spec 必须先进入 base
Contract → implementation → evidence
Skill 与 deterministic gate 职责分离
```

接受前只需要收口：

```
1. Authority hierarchy 与 partial supersession
2. accepted Spec 的不可变性和最终 review commit 绑定
3. Conformance 必须绑定 Spec/代码/环境版本
4. State、Observation、Claim 的最后一处类型泄漏
```

修完后，这套框架就足以支撑第一份：

```
AGENT_FORUM_CORE_INVARIANTS_V1
```

而且会比现在直接开始写 Core Invariants 更安全，因为身份、权限、Reviewer Gate、删除和 Finalization 恰好都是最容易出现 overlapping authority 与历史 Contract 被改写的领域。

---

## 可直接发给 PR Agent 的复审意见

```
DEVELOPMENT_GRAMMAR_AND_SPEC_GOVERNANCE_V0_REVIEW = REVISE

Direction, directory split, six-primitive grammar, spec-first base-branch
rule, lifecycle/conformance separation, and PREFLIGHT/AUTHOR/REVIEW/
COMPLIANCE modes are accepted and must not be redesigned.

Before acceptance, amend the governance bootstrap to freeze:

1. Authority precedence
   - Product Direction is a named higher-level authority.
   - Lower-level Specs may refine but may not supersede Product Direction.
   - Partial supersession is forbidden in V0 unless an explicit,
     machine-readable per-authority/per-Contract model is introduced.
   - External governing dependencies must be referenceable without
     allowing this repository to govern another repository.

2. Accepted-Spec immutability
   - accepted Decision and Contract meaning may not be changed under
     the same stable ID;
   - post-acceptance AMEND is editorial or strictly additive only;
   - normative meaning changes require SUPERSEDE;
   - Contract IDs may never be repurposed.

3. Review binding
   - every REVIEW records exact base commit, reviewed Spec commit,
     reviewer identity and final accepted head;
   - any semantic change after review invalidates the review;
   - the final accepted head must be independently rechecked.

4. Qualified conformance
   - conformance is a relation over spec revision, implementation
     commit, environment, evaluation time and evidence;
   - VERIFIED is never an unqualified permanent property of a Spec.

5. Primitive boundary
   - Current State is a versioned projection backed by Observations
     and Claims, not an unsourced factual authority;
   - replace VERIFIED CLAIM with SUPPORTED CLAIM.

Also label V0 enforcement explicitly as MANUAL_POLICY because the
deterministic verifier, base-branch gate and required branch protection
do not yet exist.

SPEC_REVIEW = REVISE
READY_TO_MARK_ACCEPTED = NO
PRODUCT_DIRECTION = KEEP
FRAMEWORK_REWRITE_REQUIRED = NO
```