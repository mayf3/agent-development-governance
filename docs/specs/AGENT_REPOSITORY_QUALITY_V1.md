---
spec_id: AGENT_REPOSITORY_QUALITY_V1
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

# AGENT_REPOSITORY_QUALITY_V1

仓库质量与开源发布基线。状态：**proposed；尚未接受、实施或分发**。

## 1. Goal

让不了解开发历史的人或 Agent，能够理解仓库职责，完成已声明的最小使用场景，并找到修改、验证和维护入口。验收实际可用性，而不是文件数量、目录外观或徽章分数。

## 2. Scope and non-goals

本标准规定源仓后续分发的仓库质量规则及其本地采用方式：模块职责、README、文档一致性、可验证使用、贡献入口和有明确触发条件的开源发布检查。

普通变更检查受影响范围；首次公开和对外发布检查完整的本次公开/发布面。非代码仓库以其实际交付物的使用与验证代替软件编译；不凭仓库名称推断适用性。

不规定统一语言、目录树、架构层数、README 长度或覆盖率阈值；不创建治理平台、评分系统、固定 Agent 阵列或额外审批角色。本 PR 不修理存量 README，不变更 accepted authority，不实施分发、CI 或消费者改造，不开源私有仓库、不选择许可证、不发布制品、不修改权限、凭据或生产状态。

## 3. Authority and dependencies

```text
AUTHORING_BASE = 9dcd0c49a5932e44e2801317b6281bdc6a168d25
PRIMARY_PARENT = AGENT_DEVELOPMENT_GOVERNANCE_V1 at AUTHORING_BASE
AUTHORITY_ACTION = NEW
PLAN_LEVEL = BRIEF
ASSURANCE_LEVEL = DURABLE
ROUTE_STAGE = AUTHORITY_AUTHORING
ACCEPTANCE_ACTOR = mayf3 or an explicitly authorized maintainer
DISTRIBUTION_IMPLEMENTATION_ALLOWED_IN_THIS_PR = NO
PRODUCTION_OPERATION_ALLOWED = NO
```

质量基线是新增独立义务，不原地改写既有 Decision/Contract。父规范的本地权威、执行授权、证据、受控操作、比例化审查和停止规则保持不变；其他 accepted 专项规范不被替代、重写或重新指定父规范。PR #16 不是本标准的依赖或权威。

外部资料仅作为设计参考，选择及限制记录于 [SOURCE_SELECTION.md](../rationale/repository-quality/SOURCE_SELECTION.md)。`external_authorities: []` 表示没有把网页或外部完整合规体系引入为可直接裁决本仓的产品权威。实际义务由本标准的 Decision/Contract 在接受后确定。

## 4. Current State

### STATE-RQ-001 — 已有治理机制，当前说明存在局部矛盾

- Subject: `mayf3/agent-development-governance` 的治理与用户入口文档。
- As of commit: `9dcd0c49a5932e44e2801317b6281bdc6a168d25`。
- Environment / observed at: GitHub 只读源文件；2026-09-15。
- Projection: 已有 accepted Governance V1；README 与 CONTRIBUTING 对 bootstrap 状态的描述不同。尚无本标准的分发实施或消费者验证结果。
- Basis: `OBS-RQ-001`、`OBS-RQ-002`；仅描述读取范围，不评价整个仓库是否适合开源。

## 5. Observations

### OBS-RQ-001 — 主线已有比例化治理与不可变权威要求

- Source / revision: `AGENTS.md`、`.agents/README.md`、`.agents/local/README.md` 及 `AGENT_DEVELOPMENT_GOVERNANCE_V1`；均为 AUTHORING_BASE。
- Environment / observed at / method: GitHub 只读；2026-09-15；读取治理入口及相关 Contracts。
- Result: 已有本地采用、隔离写入、NEW/SUPERSEDE、证据与最短授权路径规则；没有必要为文档质量另建工作流。
- Provenance: [父规范](AGENT_DEVELOPMENT_GOVERNANCE_V1.md) 的 `CTR-GOV1-001` 至 `CTR-GOV1-009`、`CTR-GOV1-012` 至 `CTR-GOV1-020`。

### OBS-RQ-002 — 两个存在的文档给出不同生命周期描述

- Source / revision: `README.md` L18-L29；`CONTRIBUTING.md` L12；AUTHORING_BASE。
- Environment / observed at / method: GitHub 只读；2026-09-15；直接对照文本。
- Result: README 写 Governance V1 accepted、bootstrap V0 superseded；CONTRIBUTING 写 bootstrap 仍 proposed。
- Provenance: 两份文件的 blob 分别为 `44c8fe36e93f0c2436acf8861bd5f2bbdabb7f5b`、`734aff522cba3f28f2faebb019264ced9aabb0b6`。不由此推断实际发布或运行状态。

## 6. Claims and assumptions

### CLM-RQ-001 — 文件存在不能证明入口描述一致

- Support state: SUPPORTED。
- Supported by evidence: `EVD-RQ-001`；contradicted by evidence: none known。
- Uncertainty: 一个局部反例只证明存在性检查不充分，不证明拟议标准已能消除所有文档漂移。

## 7. Evidence relations

### EVD-RQ-001 — 同一基线的文本对照支持存在性检查不足

- Source observations / target / relation: `OBS-RQ-002` / `CLM-RQ-001` / SUPPORTS。
- Bound coordinates: AUTHORING_BASE，两个命名文件及 blob，2026-09-15，GitHub 只读。
- Strength/sufficiency: 足以证明“两个文件都存在”不等于生命周期描述一致。
- Limitations / provenance: 不证明产品或发布合规；仅为 `OBS-RQ-002` 的文本对照。

## 8. Decisions

### DEC-RQ-001 — 约束读者任务与职责边界，而非外观

- Decision owner: repository owner。
- Decision: 要求可理解的结构、真实入口和可导航的当前文档；允许仓库采用适合自身的实现与文档布局。
- Rejected alternative / reason: 统一目录或文件打勾；形式不能替代使用与维护能力。

### DEC-RQ-002 — 区分日常质量与实际公开/发布责任

- Decision owner: repository owner。
- Decision: 日常按影响面检查；实际首次公开、对外发行及已公开面的相关变更触发相应发布要求，不能通过改标签规避。
- Rejected alternative / reason: 每次修复全量开源审计，或以“只是 demo”绕过真实公开风险；两者均偏离任务后果。

### DEC-RQ-003 — 采用明确的本地要求，不浮动继承外部清单

- Decision owner: repository owner。
- Decision: 参考 GitHub、OpenSSF、Diátaxis 和 OSI 的相关概念，但只执行本地已接受 Contracts；不宣称完整外部认证。
- Rejected alternative / reason: 自动跟随最新外部网页；会绕过本地语义审查与采用边界。

### DEC-RQ-004 — 在现有流程内以证据验收

- Decision owner: repository owner。
- Decision: 复用既有 PREFLIGHT、REVIEW、Brief 和 CI；区分机械检查、作者自查、独立语义审查与真实使用结果。
- Rejected alternative / reason: 新评分/审批平台；增加流程并不能证明文档能用。

## 9. Contracts

### CTR-RQ-001 — 适用范围和授权不可混淆

分发规则 MUST 要求消费者经 exact-commit 本地采用后才适用。日常变更 MUST 检查受影响质量表面；首次公开仓库、文档站点、源代码包或制品，以及对外发布版本，MUST 检查完整的本次公开/发布面。已公开仓库的普通修改仅检查受影响公开面，不重复全历史审计；明确全量审查及父规范要求的完整矩阵仍适用。

触发取决于实际动作和暴露范围，不取决于是否自称“release”；私有内部使用不自动触发公开义务。MUST NOT 将采用标准视为公开仓库、选择/更换许可证、变更权限、部署或发布的执行授权。

### CTR-RQ-002 — 结构必须能解释功能归属

采用者 MUST 在 README 或其直接导航的设计说明中交代仓库职责、非目标和主要入口；有多个主要模块或跨仓依赖时，还 MUST 说明模块职责及主要依赖方向。相关变更 MUST 能定位功能归属，并处理本次新增的职责重复或与已声明边界的冲突。

MUST NOT 以统一 `src/` 布局、固定分层或抽象数量代替判断；小仓库 MAY 用一段说明完成要求。内部文件组织本身不自动成为公共兼容契约；涉及已接受架构含义的改变仍走父规范的 authority 路由。

### CTR-RQ-003 — README 必须是准确、可进入的使用入口

采用者的用户入口 README MUST 直接说明或清晰链接：用途与限制；当前支持状态；最小使用步骤及成功结果；环境、配置和外部依赖；开发验证与详细文档；实际维护/反馈入口及适用的许可信息。私有项目 MAY 明示内部使用或许可尚未决定，不得伪装为已开源。

已实现、实验性、提案、未验证和计划能力 MUST 可区分，并说明所针对的源码/发布版本范围。MUST NOT 把设计 Spec、mock 结果或计划当成当前能力；MUST NOT 要求读者先阅读历史聊天、完整审查档案或 Agent 工作协议才能开始使用。`AGENTS.md` 不替代 README。

### CTR-RQ-004 — 当前文档有维护来源，并随相关行为同步

采用者 MUST 让读者区分当前使用说明/参考、当前有效权威、设计提案与历史调查/执行证据；复杂文档集 MUST 有可达的导航，规模很小时 README 即可承担导航。对同一配置、接口、安装流程或支持状态，MUST 指明维护来源；镜像、翻译和生成版本 MAY 存在，但须标明来源/版本并保持适用内容一致。

改变使用方式、接口、配置、权限、结构边界或部署步骤的变更，MUST 在同一交付变更中更新相关文档/生成源及导航。外部发布文档无法同 PR 落地时，MUST 绑定配套修订，并在相关发布前验证匹配；不能以“文档以后再写”结束交付。无相关影响的小修复不要求修改 README。

MUST NOT 通过修改说明、隐藏失败或重写历史证据掩盖实现偏离 accepted authority；历史规范不为“文档一致”而改变原有含义，采用状态说明或既有合法替代协议处理。教程、操作指南、参考和解释可分节，不强制四套目录。

### CTR-RQ-005 — 已声明的使用和验证路径必须可执行

采用者 MUST 提供其交付物的最小使用与验证路径：在干净检出/安装以及已声明环境中可执行的步骤、必要依赖/版本约束、配置示例、测试或验证命令及可观察结果。需要构建的软件 MUST 有可工作的构建入口；主要功能变更 MUST 增加或更新对应的可执行验证。非代码仓库采用对应的内容/分发验证，不假装执行编译。

环境限制、私人服务、收费服务、硬件、网络和凭据需求 MUST 在适用时明确，示例不得包含真实秘密。文档 MUST 区分可公开复现部分与受限集成部分；不强制离线运行、公开私有依赖或字节级可复现构建。没有受限环境结果时，只能报告已验证子集，相关集成仍未验证；不能以 mock 替代或用 N/A 隐去已承诺能力。

### CTR-RQ-006 — 实际公开/发布面必须具备可核对的发布材料

`CTR-RQ-001` 触发的公开/发布审查 MUST 覆盖以下适用内容，并区分源代码、文档与制品的具体范围：

- 由有权主体决定的许可与第三方材料/依赖声明，包含相应分发权限和必要 notices；声称开源时须有符合开源定义的许可依据，不能只依据 public visibility 或任意复制的 LICENSE。
- 从公开入口可找到的贡献、缺陷反馈和安全报告说明；使用真实、已由维护方确认的渠道，说明私密报告方式或实际限制，不虚构邮箱、角色、SLA 或社区承诺；该确认不要求向渠道发送试探性消息。
- 对版本化发行，明确版本、源码 commit、发布物对应关系、适用环境、重要变化和破坏性变更/迁移说明；首发无迁移时说明原因。仅首次公开源码而未发行制品时，明确“无版本化发行”，不编造发布记录。
- 明确支持状态与已知限制；当前工作树、示例、附件、日志、将公开的历史/ref 及其他实际发布物的敏感信息检查与必要内容审阅。首次公开检查实际将暴露的范围，之后可复用未失效的检查并检查增量。

必要权限、材料、敏感检查或验证证据未知时，相关公开/发布就绪状态 MUST 为 NO/UNKNOWN，不得发布或声称就绪；缺少署名、已知秘密泄露等问题不能用质量评分抵消。秘密值不得进入审查报告；泄露处置、撤销凭据或重写历史须另按现有授权执行。本标准不自动要求 CLA、签名发布或 SBOM，但 MUST NOT 弱化消费者已有此类义务。

### CTR-RQ-007 — 外部参考不产生浮动义务或认证

分发说明 MUST 记录采用的参考主题、官方来源、版本或查阅日期、本地 Contract 映射与未采用边界；可放在既有文档，不为消费者增加独立登记系统。外部网页更新 MUST NOT 自动改变本地检查、权限、角色或阻断条件。机器执行和 Reviewer MUST 以本地有效 Contract 为准，不以失效链接或未来网页的新条目现场立法。

MUST NOT 将“参考 GitHub/OpenSSF/Diátaxis”写成完整达标、认证或徽章授予。未来采用完整外部标准须明确版本、适用条目、缺口与本地接受；本版本不作该选择。

### CTR-RQ-008 — 验收必须区分事实、范围与检查能力

采用者的相关审查 MUST 指明候选版本、检查范围、环境、执行方式、结果及限制。普通变更只验证受影响规则和直接依赖；首次公开/发行、受控或完整审查按父规范检查完整适用矩阵。N/A MUST 来自条款条件，不能由“暂时做不到”替代；证据不足是未验证，不是通过。

CI MAY 检查内部链接、生成文档同步、构建、测试、最小示例与敏感信息；新检查先在明确范围验证，再按既有授权启用。MUST NOT 用文件存在、徽章、CI 绿灯或作者自查宣称结构合理、文档真实或发布就绪。一次可执行文档核查 MUST 记录实际步骤与预期/实际结果；外部网络失败须标明依赖失败，不能误报本地断链或成功。

既有无关债务不自动阻断局部修复；本次引入的矛盾和直接影响目标的缺口须处理。仍有未覆盖基线项时 MAY 完成限定范围任务，但 MUST NOT 宣称整仓达标。Blocker 仍须满足父规范的合法来源、具体反例、影响与最小修复要求；完成边界达到后停止。

### CTR-RQ-009 — 接入现有分发而非另建工作流

本标准接受后的分发实施 MUST 以已接受版本为基线，将原则接入 `.agents/README.md`，将影响判断接入 PREFLIGHT，将受影响质量检查接入 REVIEW，并复用现有 Change Brief / Review Record 模板。最小条件性说明为“结构影响、文档影响、验证、公开影响”；不适用时简短理由即可，不增加普通任务空表或额外审批。

分发内容 MUST 在消费者已取得的文件内自足，不能依赖未分发的源仓 `docs/specs/` 或本 rationale 路径；分发变更须同步现有版本/manifest 并验证 exact-commit vendor round trip。实施验收 MUST 包含本治理仓库和一个经授权的代码仓库/隔离副本，验证真实使用任务、文档矛盾反例及普通修复不过度阻断。

源仓接受、分发实施/发布、消费者本地采用、实际仓库/发布面合规 MUST 分别记录。仅接受此 Spec 不等于上述后续工作完成，也不授权自动修改所有消费者；此 authoring PR MUST NOT 先行实施上述分发。

## 10. Acceptance

以下是未来验收定义，不是已执行结果。作者案例见 [SCENARIO_REVIEW.md](../rationale/repository-quality/SCENARIO_REVIEW.md)，不替代独立审查或运行证据。

### ACC-RQ-001 — 适用范围和实际公开触发

- Contracts: `CTR-RQ-001`。
- Method: 分别判定私有小修复、公开仓库局部变更、首次公开含历史仓库、标为 demo 的实际制品发行。
- Environment: exact candidate 与隔离情景；无真实公开操作。
- Required evidence: 每例动作、暴露范围、适用条款与授权判断。
- Expected result: 私有变更不触发发布；实际公开不因改名绕过；只有有效另行授权允许执行。
- Failure condition: 自动公开、全局清扫、因缺 LICENSE 卡住无关私有修复，或 demo 规避发布检查。

### ACC-RQ-002 — 结构可解释而不强制分层

- Contracts: `CTR-RQ-002`。
- Method: 从入口定位小工具的功能和多模块服务的主要依赖；加入一条违反已声明边界的变更。
- Environment: 经授权的 exact-revision 示例/代码仓库。
- Required evidence: 入口、模块/依赖说明、变更归属、正反例判断。
- Expected result: 小工具可用简短说明通过；真实边界冲突被识别。
- Failure condition: 凭目录名字通过，或为无必要层级重构制造 blocker。

### ACC-RQ-003 — README 真伪与文档一致性

- Contracts: `CTR-RQ-003`、`CTR-RQ-004`。
- Method: 检查一项能力和一项配置变更；注入 README/CONTRIBUTING 生命周期冲突、旧配置文档及提案冒充已上线能力。
- Environment: exact candidate；源仓例子使用 `OBS-RQ-002` 坐标。
- Required evidence: 使用入口、事实来源、相互引用、配套文档 diff、冲突判断和未知项。
- Expected result: 当前能力/提案分清；相关说明同步；历史权威和证据未被改写；无影响任务不强改 README。
- Failure condition: 只看文件齐全，靠改文档遮掩实现违约，或未同步公开参考便宣布完整交付。

### ACC-RQ-004 — 可执行使用与验证

- Contracts: `CTR-RQ-005`。
- Method: 在声明环境按公开步骤从干净检出/安装完成最小场景及验证；检查受限依赖与 mock-only 的反例。
- Environment: exact source/build、临时目录及声明依赖；不得借用未声明的作者机器状态。
- Required evidence: 工具/依赖版本、配置类别、命令、预期/实际结果及受限部分的独立可审阅脱敏证据或未验证标记。
- Expected result: 已声明范围可执行；代码与非代码按各自交付物验证；无法执行部分不被冒充通过。
- Failure condition: 命令不存在、隐含路径/服务、错误成功判据、mock 冒充集成或未运行被写成 PASS。

### ACC-RQ-005 — 公开/发布完整性与权限边界

- Contracts: `CTR-RQ-006`。
- Method: 审查一个只公开源码的包和一个带制品的版本发行；注入缺失许可依据、伪造安全渠道、制品/源码错配及仅历史中含合成测试秘密的反例。
- Environment: 隔离发布包；用无效测试标记，不使用真实凭据或实际公开操作。
- Required evidence: 适用范围、许可/notice 依据、维护方渠道确认、版本/commit/制品映射、变更/迁移说明、敏感检查范围与结果、未知项处置。
- Expected result: 仅适用材料必需；未知或失败阻止相关公开/发布就绪；无许可证选择、权限或生产副作用。
- Failure condition: 无证据声明可开源，以工作树干净推断历史干净，以高分掩盖缺陷，或擅自更改许可/凭据。

### ACC-RQ-006 — 外部来源更新不改变本地规则

- Contracts: `CTR-RQ-007`。
- Method: 核对来源选择表，再模拟参考网页增加条目或失效。
- Environment: 候选 Spec 和固定的来源说明；不改真实网页。
- Required evidence: 来源版本/日期、本地映射、未采用边界及前后判断。
- Expected result: 本地义务不浮动；完整 OpenSSF 达标声明被拒绝。
- Failure condition: 新网页条目成为现行 blocker，或借引用声称认证。

### ACC-RQ-007 — 比例化证据与不过度阻断

- Contracts: `CTR-RQ-008`。
- Method: 比较局部修复与首次发布；分别注入旧无关债务、当次文档矛盾、未知受限验证和仅存在文件的绿灯。
- Environment: exact candidate 的情景审查；实施时使用实际记录与检查结果。
- Required evidence: 每例范围、适用理由、结果、限制与 blocker 合法依据。
- Expected result: 局部目标可独立完成，整仓未验证仍明确；当次真实问题被识别；未知不变成 N/A/PASS。
- Failure condition: 无关债务无限扩张、文件检查冒充语义审查、豁免既有强制安全门或无依据报告就绪。

### ACC-RQ-008 — 分发接入与试用闭环

- Contracts: `CTR-RQ-009`。
- Method: 接受后的独立实施阶段核对开发入口/模板、manifest/版本、干净消费者 vendor round trip；源仓与一个经授权代码试点按文档实际使用并检查正反例。
- Environment: exact accepted Spec、distribution commit、consumer commit 和隔离环境。
- Required evidence: 入口 diff、分发摘要、vendor/既有测试结果、两个试点的实际步骤、文档修正、反例记录及分阶段状态。
- Expected result: 消费者不依赖缺失源仓文件；最小质量要求进入既有流程；无新增审批平台或自动消费者迁移。
- Failure condition: 只新增 Spec 就声称启用、消费者链接不可达、试点只做文件清点或把未执行写成完成。

## 11. Alternatives and disposition

全量外部徽章合规、统一架构/目录、给每次 PR 增加全仓审计、仅补齐 README/LICENSE、强制所有仓库公开、自动引入最新网页规则均不采用；原因分别为范围失控、外观替代结果或授权越界。签名/SBOM/社区规则可由后续具体发布需求决定，既有义务不受本标准影响。

## 12. Migration, compatibility, and rollback

本 PR 仅标准提案、来源/案例和索引。独立审查及 Owner 对 exact candidate 的接受在前，分发实施与试点在后；消费者仍逐仓固定版本、本地接受。该流程不替代父规范的最终 HEAD 检查与主线生效规则。

本标准的基线采用检查记录范围与未解决项；先修本次目标直接相关问题，不制造全仓同时翻修。没有完整证据不得声称整仓或公开就绪。已有历史规范与审计记录不批量改写；旧入口文档的错误在后续获授权的试点修正，不在此提案中顺带修改。

分发回退须按既有授权恢复已知版本并核对消费者 pin；不得静默关闭原有强制门。撤销治理版本不撤销已经作出的公开承诺，也不能收回已经公开的信息。本标准不授权历史清除、权限调整或生产回滚。

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE within the proposed rule design; exact-head acceptance remains pending
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE identified in the bounded authoring review
PARTIAL_SUPERSESSION = NONE
INDEPENDENT_REVIEW = NOT_PERFORMED
DISTRIBUTION_IMPLEMENTATION = NOT_STARTED
CONSUMER_ADOPTION = NOT_PERFORMED
REPOSITORY_OR_RELEASE_CONFORMANCE = NOT_EVALUATED
```

具体试点代码仓库、实现工具与各产品许可证/发布目标由后续获授权任务选择；不是本提案对其操作的预授权。来源表和作者情景不能作为独立语义审查证明。
