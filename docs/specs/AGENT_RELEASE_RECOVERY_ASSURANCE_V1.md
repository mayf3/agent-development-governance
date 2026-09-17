---
spec_id: AGENT_RELEASE_RECOVERY_ASSURANCE_V1
status: proposed
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance
governed_by:
  - AGENT_DEVELOPMENT_GOVERNANCE_V1
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# 发布与恢复验证标准

## 1. Goal

把发布组成、对象权限、失败前态和验证边界前移到设计与审查，避免在生产反复发现未建模的组合状态。

> 同一产物接受验证与安装；权限按对象角色定义；失败后的状态也是下一次操作的正式输入；测试不能抹去它声称验证的关键差异；回滚不能抹去已发生的业务事实。

目标是减少需要人工协调的发布关系、竞争写入入口和历史耦合，而不是减少安全证据、放宽精确审查或规定统一架构。

## 2. Scope and non-goals

本标准约束治理分发如何识别、设计和验证发布、安装、切换、恢复，以及其依赖的权限、持久化状态、兼容性与故障兜底变更。它也适用于新增这些机制的开发阶段，不只适用于最终操作。

不规定所有产品采用四个模块、root owner、特定 UID/GID、launchd、固定目录、单个 JSON、物理单文件 manifest/journal、全系统大锁或新 supervisor。不同生命周期、独立版本与合法多身份保留。

不实现 Scheduler 修复，不授权部署、删除、权限/凭据变更、恢复未知执行、清理备份或消费者批量升级；不修改已接受规范；不要求所有任务执行发布矩阵、填空表、增加审批或建设发布平台。

## 3. Authority and dependencies

```text
AUTHORITY_ACTION = NEW
PARENT = AGENT_DEVELOPMENT_GOVERNANCE_V1
PARENT_REVISION = e123130562774cafb78bb212a9b54d7f10658c4f
RELATED_ACCEPTED_AUTHORITY = AGENT_MODEL_CONVERGENCE_V1
RELATED_AUTHORITY_REVISION = e123130562774cafb78bb212a9b54d7f10658c4f
ROUTE_STAGE = AUTHORITY_AUTHORING
PLAN_LEVEL = BRIEF
ASSURANCE_LEVEL = DURABLE
IMPLEMENTATION_AUTHORITY = governance-distribution Contracts only, after acceptance
ACCEPTANCE_ACTOR = mayf3 or an explicitly authorized maintainer
```

父规范的本地权威、受控授权、证据、独立审查、accepted 语义不可变与 stop controls 保持原义。新增的是发布/恢复边界和风险维度的明确设计、验证义务，不以 NEW 覆盖任何既有产品 Contract；冲突必须回到拥有该语义的 authority 路由。

[历史模型收敛标准](AGENT_MODEL_CONVERGENCE_V1.md) 已决定重复模型识别、临时桥接退出及旧路径不复活。本标准复用这些要求，不复制一套迁移生命周期。仓库质量提案 PR #17 不是本标准权威或前置依赖，本 PR 不修改它。相关规范均以本节 revision 为本次 authoring 坐标。

附件审计是非权威设计输入，不是外部 Product Authority。[来源摘录与映射](../rationale/release-recovery/SOURCE_MAPPING.md) 区分原文、报告解释和本地新增要求。接受、分发实施/发布、消费者采用、具体运行态验证分别记录；本 authoring PR 只提出规范。

## 4. Current State

### STATE-RRA-001 — 已有安全边界，新增发布验证义务尚为提案

- Subject / revision: `mayf3/agent-development-governance@e123130562774cafb78bb212a9b54d7f10658c4f`。
- Environment / observed at: remote main 与当前对话，2026-09-16。
- Projection: Governance V1 和历史模型收敛标准已 accepted；本任务提出限定的新标准，没有证据证明其分发、消费者采用或产品修复已完成。
- Basis: `OBS-RRA-001`、`OBS-RRA-002`。

## 5. Observations

### OBS-RRA-001 — 接受的规范保留操作、证据与减法边界

- Source / revision: 父规范、`AGENT_MODEL_CONVERGENCE_V1`、`AGENTS.md`、`.agents/README.md`、local governance 和 Spec-governance 规则，绑定本节 main revision。
- Environment / observed at: GitHub 只读与同一不可变版本的会话材料，2026-09-16。
- Method / result: 核对当前 main、规范索引与规则；既有要求包含授权、独立复核、限定验收和历史退场，不能因本提案而弱化。
- Provenance: 上述路径在 `e123130562774cafb78bb212a9b54d7f10658c4f`；索引 blob `cc0a40733141b5bfc4c04f950098ebb21e7d0592`。

### OBS-RRA-002 — 提供的审计描述了发布/恢复复杂性来源

- Source: 2026-09-16 用户提供的 586 行审计摘要；原始 UTF-8 文件 SHA-256 `138bc81db3fa162768d0db3648db6dbee7a0e1223746983c034cf76a7af50bb3`。
- Method: 阅读所给全文、核对原始字节，并在 SOURCE_MAPPING 保留相关逐字摘录及原行号。
- Result: 文本讨论 ownership 碎片、source/payload/CLI 绑定、失败前态、fixture 消除关键差异、分层验收与 W2 共享故障面。
- Limits: 附件自报 `LIVE_PRODUCTION_READBACK=NOT_PERFORMED`、`TESTS_EXECUTED_BY_AUDITOR=NO`。本任务没有独立复现产品故障，未读取附件内另链的完整审计和 JSON，不能据摘要宣称检查了其全部组件/债务字段。
- Provenance: SOURCE_MAPPING 的存储摘录是本提案可审查的输入快照；原文摘要校验值仅用于同一性核对，不替代缺失的完整审计或运行证据。

## 6. Claims and assumptions

### CLM-RRA-001 — 前移边界与风险维度检查可针对报告中的返工机制

- Support state: INFERRED。
- Supported by evidence: `EVD-RRA-001`。
- Contradicted by evidence: 本次未取得实测反证。
- Uncertainty: 这是拟采用的设计选择，未测量事故率、工时或返工次数下降；不把报告中的 generation、review、apply 和 closure 计数混为生产失败次数。

## 7. Evidence relations

### EVD-RRA-001 — 文本支持提出有界预防规则，不证明生产闭环

- Source observations: `OBS-RRA-001`、`OBS-RRA-002`。
- Target / relation: `CLM-RRA-001` / SUPPORTS。
- Bound coordinates: 本节治理 revision；SOURCE_MAPPING 在本候选提交中的摘录 S1–S8 及原文 SHA-256/行号。
- Sufficiency: 可核对原文如何引出本地提案，以及为何需要保留既有安全边界。
- Limitations: 不是因果实验、生产 incident、successor 映射、精确部署状态或实现符合性证明。
- Provenance: [SOURCE_MAPPING](../rationale/release-recovery/SOURCE_MAPPING.md)。

## 8. Decisions

### DEC-RRA-001 — 先定义发布与对象角色，再增加入口

- Decision owner: repository owner，proposed for acceptance。
- Decision: 同一交付单元明确组成、兼容关系、验证产物和安装身份；权限按对象类别及实际读写者定义，相关入口遵守同一变更域协议。
- Rejected alternative: 用当前用户、目录属组、脚本常量或临时 handoff 隐式拼装发布。
- Reason: 多个正确局部产物仍可能形成不一致的安装组合。

### DEC-RRA-002 — 失败前态和不可回退事实必须在操作前建模

- Decision owner: repository owner，proposed for acceptance。
- Decision: 将部分提交和失败后的实际状态作为输入，区分可回滚发布状态与已发生业务事实，明确 resume、abort 和受控恢复边界。
- Rejected alternative: 反复从干净目录测试，或用旧代码覆盖来宣称业务从未执行。
- Reason: 失败/回滚不保证恢复初始前态，也不自动确定未知业务结果。

### DEC-RRA-003 — 验证只证明保留的风险维度与实际路径

- Decision owner: repository owner，proposed for acceptance。
- Decision: 风险相关权限、历史 metadata、部分状态与依赖故障必须有对应验证；mock、canary 和隔离声明只承载实际覆盖的结论。
- Rejected alternative: 以统一身份、no-op shim、空历史或进程名称证明真实权限、恢复和独立性。
- Reason: 测试通过不能补回被测试环境抹掉的关键差异。

### DEC-RRA-004 — 复用现有治理，先减依赖而非追加平台

- Decision owner: repository owner，proposed for acceptance。
- Decision: 将条件性问题接入现有开发/操作记录；已有合同内的修复不重新立法，真实新语义缺口走既有 PREFLIGHT；标准与分发、采用、生产效果分别验收。
- Rejected alternative: 每次故障新增全局普查、固定审批、另一个 watchdog 或兼容平台。
- Reason: 治理应减少长期维护面，并在限定目标完成后停止。

## 9. Contracts

### CTR-RRA-001 — 有界适用与现有授权

Basis: `DEC-RRA-004`。

分发 MUST 在发布组成/入口、安装身份/权限、持久化操作前态/恢复语义，或独立兜底承诺发生相关变更时触发本标准；设计阶段即识别影响面，不能只在部署失败后补写。小型无关变更 MUST 保留短路径，不要求空矩阵或全仓普查。

实现/操作 MUST 依拥有该语义的 accepted Contracts 与有效 mandate；本标准不提供产品部署、身份、删除或执行恢复授权。若必需的长期语义未决定，MUST 按父规范标记 load-bearing SPEC_GAP 并停止依赖它的 readiness；已定义合同的实现缺陷 MUST 按其既有路线修复并补相关验证，不自动新建 Spec。

### CTR-RRA-002 — 同一发布单元有明确组成和变更协议

Basis: `DEC-RRA-001`。

开发者 MUST 明确本次共同交付的代码、payload、CLI、安装辅助物、配置引用及兼容前态，记录可核对的版本/摘要与相互关系；可复用已有发布记录，不要求单个物理 manifest。配置和独立服务 MAY 单独版本化，但必须声明适用兼容组合，不能强迫所有 ID 相等。

验收测试和实际安装 MUST 对应同一受审发布产物及其已声明配置绑定；测试后重新构建、换 pin 或替换文件不能自动继承旧结果。安装前 MUST 验证实际输入身份与受审组合相符；发现不匹配时停止该安装，不以源码 SHA 相同替代产物证明。后续运行结论还需核对实际加载的组件身份，不能只读磁盘目标。

触及同一变更域的多个入口 MUST 共享一致的写入资格、前置条件、互斥及恢复协议，并在取得相应互斥后重新读取关键前态。不得各自使用不协调的锁/回执来独立裁决同一事务；不要求无关变更域共用一个大锁。新增 wrapper 不自动证明旧竞争入口退出，退出按已有收敛标准验证。

### CTR-RRA-003 — 对象权限合同不由执行者身份偶然决定

Basis: `DEC-RRA-001`。

权限相关变更 MUST 按对象类别说明临时创建者、安装后 owner、writer、reader、必要 metadata 与目标平台路径/copy/restore 规则，区分 candidate、target、preimage、运行状态和证据。不得无声明地将当前进程身份、临时目录属组或另一对象 owner 推导成目标 reader/owner。

验收 MUST 以声明的真实 reader/writer 角色检查操作系统访问和应用安全校验两层；涉及的平台特性按实际风险保留，例如 UID/GID/mode、ACL/xattr、umask、symlink 或已加载服务。root 可访问不替代应用 gate，应用配置允许也不替代实际访问。无法执行关键角色/平台检查时相关结论为未验证，不能从单一身份 shim 得出通过；不强制所有平台使用同一账户或 metadata。

### CTR-RRA-004 — 失败前态、重入与回滚事实边界完整

Basis: `DEC-RRA-002`。

多阶段持久化操作 MUST 在执行前定义其支持的起始状态、可能的部分提交/失败 generation、可观察的提交边界、重复执行/继续/abort 行为，以及哪些状态可回滚、哪些事实必须保留。preimage MUST 覆盖相关内容、metadata、路径/链接和加载状态，不能默认只是旧文件字节。

失败后再次操作 MUST 核对实际状态与事务身份，不复用已失效的首次前态；已发生的副作用及结果未定的步骤不得当成“从未执行”而盲目重跑。无法判定安全下一步时必须保留证据、按已有合同停止或有界隔离；不通过清空状态获得重试资格。只在实际持有的授权范围内执行恢复。

回滚 MUST 保留拥有该事实的合同要求保留的执行、已接受通知/投递、去重、incident 和审计事实，验证旧版本对保留状态的兼容性；不兼容时停止该回滚或执行已有授权的替代处置。代码恢复不能自动清除 fence、确定业务结果或授权重跑。执行结果、精确终止证明、delivery 结果和承载进程生命周期 MUST 按产品合同保持区分；本标准既不要求所有系统保留同名模型，也不要求每次终止证明都杀掉常驻进程。

### CTR-RRA-005 — Fixture 保留其结论依赖的关键差异

Basis: `DEC-RRA-003`。

相关验证 MUST 记录结论依赖的风险维度，并区分真实保留、模拟和未覆盖：例如多身份权限、历史 metadata/数据、旧链接、partial preimage、失败 generation、已发生副作用和宿主行为。允许 mock/shim，但被消除的关键差异不能计入该能力的已验证结论。

生产相关结论 MUST 有覆盖必要维度的隔离环境结果或父规范允许的可审查、脱敏、绑定坐标的独立执行证据；不能将无法取得证据记成 N/A，也不能为补证据擅自操作生产。新发现的关键前态 MUST 进入下一次相关回归验证，或明确记录该必需验证尚未完成并阻止相应就绪声明。MUST 按风险与实际反例选最小有效组合，不要求无界穷举所有平台状态。

### CTR-RRA-006 — 分层验收不得放大 PASS

Basis: `DEC-RRA-003`。

关键检查 MUST 绑定被证明的主张、实际执行路径、产物/配置、环境/身份、预期与实际结果、时间及限制；源代码、磁盘安装、运行加载、组件可用、业务执行、结果投递和恢复各结论分别举证。整体完成必须满足本次已声明业务目标的所有必要环节，不能通过事后缩小目标隐藏未验证路径。

native/no-op canary、单个阶段 PASS、命令 exit 0、generic health 或 CI 通过不得自动提升为端到端恢复。接单/发送确认不等于业务执行完成；unknown 不能变成失败或安全重跑许可，终止证明不等于业务结果。N/A 必须由条款与目标的真实适用条件支持，缺证据为未验证；日常变更可以完成限定范围，但不得据此报告整套生产系统已恢复。

### CTR-RRA-007 — 独立兜底声明有实际故障边界

Basis: `DEC-RRA-003`。

声称独立监控、隔离或恢复兜底的设计/变更 MUST 声明覆盖的故障集合、共享依赖、最小报告路径及盲区；不同进程、目录或名称不构成独立性证据。MUST 在经授权的隔离环境或等效可审查执行证据中，验证被覆盖依赖失效后兜底路径仍能观察并报告承诺结果；不能只证明监控进程存活。

未覆盖故障 MAY 明确列为盲区，但不得削弱已有 accepted 承诺来制造通过；收窄承诺须走其 authority 路由。修复优先消除不必要共享依赖，不因本条自动增加新的 watchdog、消息系统或 supervisor。

### CTR-RRA-008 — 复用减法标准与有界缺口处理

Basis: `DEC-RRA-004`。

历史模型、一次性纳管/迁移热依赖、重复状态源和竞争 apply 入口的退出 MUST 复用 `AGENT_MODEL_CONVERGENCE_V1` 的事实归属、真实消费者、退出条件与新可用/旧退出/不复活要求，不新增平行台账。旧材料仍有运行、去重、恢复或审计用途时，不得先删以制造干净状态；脱离热依赖须先证明其必要事实由当前模型保留。

出现未定义权限/状态/恢复语义时，仅停止依赖该缺口的推进并回到既有 PREFLIGHT；无关工作不因反例被升级为全系统重构。纯实现缺陷按现有合同修复。既有复核与精确绑定不能因返工成本而取消；无关 main 变化只做有界影响检查。限定 DONE_WHEN 达到且无 EXPANSION_TRIGGER 时 MUST 停止。

### CTR-RRA-009 — 在现有开发入口实施，阶段分别验证

Basis: `DEC-RRA-004`。

接受后的分发实施 MUST 将原则接入 `.agents/README.md`，将条件性影响识别接入 PREFLIGHT，将对应验证接入 REVIEW，复用现有 Change Brief / ExecPlan / Controlled Runbook / Review Record 中适用的表面。最小问题为：发布组成与入口；对象角色；失败前态与回滚事实；保留的风险维度；主张与证据范围；兜底依赖（仅适用时）。不得强制每个任务生成全部文档、空表、新审批、评分服务或固定 Agent 编组。

分发 MUST 在既有 vendored 文件内自足，包含所依赖的收敛规则与合法来源，不依赖消费者拿不到的源仓 docs 或附件；不另建 authority 副本。变更分发须按已有规则同步版本/manifest，执行完整性/路由检查与 exact-commit vendor round trip，并在隔离案例中实际验证风险被保留、错误完成声明被拒绝、无关小修复不受额外门槛。工具只能报告实际实现的检查能力。

源仓接受、分发发布、消费者 exact-revision 本地采用、产品源码/部署/业务恢复 MUST 分别记录；未采用或未验证不得报告为已生效。本 authoring PR MUST NOT 修改 active 分发、其他规范生命周期、消费者或生产，也不得以 proposed 标准阻断其他产品。

## 10. Acceptance

[作者案例](../rationale/release-recovery/SCENARIO_REVIEW.md) 是桌面反例自查，不是运行测试或独立语义通过。以下方法须在对应阶段实际执行；本提案定义它们，不宣称完成消费者验证。

### ACC-RRA-001 — 触发有界且不改变授权

- Contracts: `CTR-RRA-001`、`CTR-RRA-008`。
- Method: 比较普通文档修正、合同内 installer bug、未定义 reader 权限、已有迁移备份热依赖四例。
- Environment: exact candidate 文本审查；后续治理分发隔离 canary。
- Required evidence: 输入、既有 authority/mandate、影响范围、路线及未完成项。
- Expected result: 无关任务短路径；实现缺陷不新建 Spec；真实缺口停止依赖路径；未证明事实保留前不删备份。
- Failure condition: 任意 case 自动全局 census、新审批或生产删除，或忽略必要语义缺口继续操作。

### ACC-RRA-002 — 验证和安装产物一致，入口协调

- Contracts: `CTR-RRA-002`。
- Method: 对一个合法发布组合验证 stage/install/load 对应；注入旧 payload、独立 CLI 漂移、配置错配、检查后输入变化和竞争入口。
- Environment: 经授权的隔离安装环境，不访问生产。
- Required evidence: 发布组合/摘要、输入校验与加载读回、互斥与 fresh precondition 结果、反例无越界写入结果。
- Expected result: 合法兼容组合通过；错配不安装，竞争入口遵守同一变更域协议；独立版本不必数值相等。
- Failure condition: 同一源码 SHA 掩盖不同产物，或锁/回执各自裁决、验证后换产物仍沿用 PASS。

### ACC-RRA-003 — 角色权限与平台差异真实覆盖

- Contracts: `CTR-RRA-003`、`CTR-RRA-005`。
- Method: 分开 creator、target owner、reader 验证 OS 访问与应用 gate；加入一个适用 metadata/路径反例，并与统一身份/no-op chown 的 fixture 比较。
- Environment: 目标平台的授权隔离多身份环境；无法取得时按父规范提供独立脱敏执行证据，否则未验证。
- Required evidence: 角色/metadata 合同、实际身份、命令和应用读取结果、真实/模拟/未覆盖维度及限制。
- Expected result: 合法访问通过；错误角色或 metadata 被识别；简化 fixture 不被当作多身份验证。
- Failure condition: root 可读替代 reader 证明，或预清理关键 metadata 后仍声称验证该风险。

### ACC-RRA-004 — 失败后重入与事实保留

- Contracts: `CTR-RRA-004`、`CTR-RRA-005`。
- Method: 在声明的关键提交边界中断隔离操作；保留部分状态、已接受通知/业务副作用和未知结果，再读取实际前态进行合法 resume/abort/rollback；检查旧版本兼容。
- Environment: 授权隔离环境或可审查独立执行证据；不恢复真实未知任务。
- Required evidence: 前态、事务身份、提交事实、故障点、各操作前后结果、无重复副作用和保留事实证明。
- Expected result: 失败后不是默认空白；不兼容 rollback 停止；未知结果诚实保留，不授权重跑或伪造终止。
- Failure condition: 清空 ledger/dedupe 得到成功，复用失效 receipt，恢复旧代码即清 fence，或强制常驻进程退出冒充产品终止合同。

### ACC-RRA-005 — 验收结论不超出路径覆盖

- Contracts: `CTR-RRA-006`。
- Method: 对 no-op canary 成功但实际执行/投递未测、磁盘已更新但进程仍旧、接单后无完成、终止已证明但结果 unknown 四例检查完成声明。
- Environment: exact completion records 与后续隔离验证路径。
- Required evidence: 原定目标、每项主张对应的实际路径/结果和未覆盖边界。
- Expected result: 只报告已验证层；原定端到端目标有未覆盖环节时不能报告完成。
- Failure condition: canary/CI/health PASS 自动升级成业务恢复，或事后缩目标、滥用 N/A 隐去缺证据。

### ACC-RRA-006 — 兜底能报告其承诺覆盖的故障

- Contracts: `CTR-RRA-007`。
- Method: 注入一个声明覆盖的主系统依赖故障，验证兜底最小报告路径；对共享同一损坏依赖的反例判定。
- Environment: 授权隔离测试或同等可审查独立执行证据。
- Required evidence: 覆盖故障集合/共享依赖图、注入点、观察与报告结果、明确盲区。
- Expected result: 仅在承诺范围内确认独立性；反例被拒绝，不通过改名或新增第三个监控自动通过。
- Failure condition: 只证明进程分离/存活，隐瞒共同依赖，或擅自削弱既有隔离承诺。

### ACC-RRA-007 — 分发自足并真正进入现有流程

- Contracts: `CTR-RRA-009`。
- Method: 检查后续分发 delta，执行 exact-commit vendor round trip；运行相关发布、失败恢复、无关小修复三类隔离任务。
- Environment: accepted Spec、后续分发候选及临时 consumer，不修改真实消费者。
- Required evidence: README/mode/template 条件性接入、来源在消费者可达、版本/manifest/路由结果、canary 输入与实际输出。
- Expected result: 相关任务提前核对边界；错误声明被拒绝；无关任务无空表/新审批。
- Failure condition: 仅合入文章就宣称分发完成、引用未分发 authority、重复台账或工具假称语义认证。

### ACC-RRA-008 — 来源与阶段不越界

- Contracts: `CTR-RRA-001`、`CTR-RRA-006`、`CTR-RRA-009`。
- Method: 核对 authoring 完整 diff、报告摘录和来源映射；挑战“报告目标等于当前生产事实”“摘要等于完整审计”“Spec 合并等于部署恢复”三种陈述。
- Environment: exact source candidate，后续采用/操作记录各自绑定坐标。
- Required evidence: 原文摘录与行号/摘要值、原文限制、本地推导标记、实际变更路径及各阶段记录。
- Expected result: 未实施保持未实施；未验证保持未验证；产品建议没有被固化为通用 UID/GID/架构/锁布局。
- Failure condition: 提案提前激活、改写已有 accepted 语义、发布原文未提供的事实或把作者自查冒充独立审查。

## 11. Alternatives and disposition

只添加事故复盘而不接入开发入口，不能作为最终分发交付。把全部 24 条债逐一升级为标准、合并所有 ID/状态、强推 root owner 或统一四模块架构，均拒绝；这些是报告的产品情境或目标，不是通用治理决定。取消精确审查、通过更干净 fixture 降低失败率、给旧入口外包一层 wrapper，不能替代有效收敛。

不进行穷举平台测试，也不引入通用发布控制平台、额外审批或实时治理服务；复用当前清单、模板、CI 和相关证据即可。

## 12. Migration, compatibility, and rollback

本 PR 仅创建 proposed 标准、来源/案例和索引。独立审查及 Owner 接受后，另一个有界分发任务实现 `CTR-RRA-009`，不得把本次提出当作实施或回写产品授权。既有收敛标准的未完成分发由其原有范围继续跟踪，不因本 PR 被报告完成。

消费者按 exact revision 本地采用后，从下一项受影响工作开始应用；不追溯重写旧证据，不因上游标准合并自动停止生产或清理历史。改变任何现有支持/权限/恢复语义仍由产品仓接受；产品回滚需其兼容性和授权，不能以恢复旧发布来撤销已发生业务事实。

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
```

以上表示提案未故意悬置承载本地规则的设计选择，不代表独立审查或 Owner 接受已完成。它们仍待 exact-candidate 流程；真实产品角色、平台约束、checkpoint、故障集合、迁移和生产操作由各拥有者按已接受合同或必要新决定处理。
