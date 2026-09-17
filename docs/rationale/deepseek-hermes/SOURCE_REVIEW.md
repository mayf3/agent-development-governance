# DeepSeek Harness 与 Hermes：来源、比较与本地取舍

记录日期：2026-09-18。性质：非权威研究与设计参考；不是外部项目审计、性能复现或新产品 Contract。配套 [实操指南](../../guides/EVIDENCE_LED_REFACTORING.md) 与 [作者案例](SCENARIO_REVIEW.md)。内容为本次原文阅读后的概括和本地适配，不复制完整 Skill。

## 1. 读取坐标与限制

| 对象 | 本次固定坐标 | 实际读取范围 |
|---|---|---|
| 本治理仓库 | `99ad23923f341d7490af2b785322032507eca910` | 现有入口、相关权威和 README；不做全仓审计 |
| `deepseek-ai/deepseek-harness` | master `ddefc45fbc7f8e46dd73185e68295696d1297887` | 七份完整 Skill，以及根 AGENTS.md 第 1–140 行和技能目录 |
| `NousResearch/hermes-agent` | main `77fb7f0a709b4df2c17822da3a08f8c93de3b3fb` | simplify-code 与 dynamic-workflow；官方 PR/复盘另按读取日期限定 |

这些是当次查询默认分支所得快照，不表示永远最新。Hermes 搜索曾返回较早的 `d04f6f791372f77c7df5e779f6fa2de2e3860d72`；simplify-code 全文从该点读取，随后在上述新 main 核对得到相同 blob，因此该文件内容比较成立，不推及整个旧树。

用户指定的路径确认为 `.agents/skills/dsh-find-simplifications`，不是 `.agnets`。同名第三方镜像有旧版描述，本次内容以官方固定提交为准。例如当前 simplification Skill 保留双 LLM adapter 的有意设计，同时将 JSONL 表述为唯一第一方 session provider，并保留对树外 provider 的中立接口；不能拿旧版“双 persistence backend”描述当当前政策。

[Refactoring Hermes with 1393 Agents 博客](https://nousresearch.com/refactoring-hermes-with-1393-agents/)的正文在本次工具中未能取得。以下以官方 PR、后续复盘和当前 Skill 为依据，**不声称完整读过博客，不用转载补全原文**。PR/Issue 正文可变；下文是 2026-09-18 读取所得的署名概括，不是原始会话数据库或不可变网页全文快照。

## 2. DeepSeek：七份 Skill 的方法和限制

### D1 — 找有证据的简化候选

[官方 dsh-find-simplifications](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/skills/dsh-find-simplifications/SKILL.md)要求追踪实际消费者、原始目的和当前成本，偏好少量强候选；既看代码，也看状态、接口、测试、配置及说明。测试/文档的存在不单独证明产品需要，静态无引用也不证明动态或外部消费者不存在。维护良好的依赖或内建能力可以替换手写实现，但剩余 glue 和保留理由也计入成本。

本地借鉴：候选记录加入消费者分类、最强反对理由、待退役维护面、反证与退出验证；复用 Model Convergence，而不复制 DeepSeek 的 pre-stable API 或特定 adapter/persistence 选择。

### D2 — 审查行为、实际入口和独立观察

[官方 dsh-code-review](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/skills/dsh-code-review/SKILL.md)强调 exact base/head、接口双方、执行处拒绝路径、真实 Loader/bin/worker 与生命周期。跨组件 invariant 应观察能够分别出错的关系，不能把组件存在或同一操作自证包装为更强证明。

本地借鉴：把审查视角落实到拒绝路径、来源和真实装载；保留有价值的简单装载测试，但标明其能力范围。不移植其特定框架注册、UI 本地化或全体 prose 阻断清单。

### D3 — CI 中的资源与并发可靠性

[官方 dsh-ci-test-reliability](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/skills/dsh-ci-test-reliability/SKILL.md)区分测试、文件、进程、job 和共享宿主拓扑；要求原子分配资源、立即注册清理、精确恢复全局状态、显式同步和静默完成。压力测试不能替代确定性的回归反例；重试、睡眠或无依据放宽超时不等于根因修复。

本地借鉴：给并行重构和测试整合加入资源清单与负例思路；平台特例、外部瞬时故障及合法预算调整保留明确范围，不统一要求同一个 runner 或禁用所有 retry。

### D4 — 精简 prose，保留完整命题

[官方 dsh-prose-standard](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/skills/dsh-prose-standard/SKILL.md)要求保留主体、动作、时序、条件、模态、例外与后果；可删执行旁白，不能删防止错误修改的理由。可见字符串和 prompt 按行为审查。

本地借鉴：文档减法与代码减法共用语义保持原则，避免把“少字”设为目的。该 Skill 的 vendor/归档目录排除和交互模式不直接成为本地永久规则。

### D5 — 用户入口与派生文档

[官方 dsh-doc](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/skills/dsh-doc/SKILL.md)从读者任务、前置条件、结果与恢复路径组织说明；当前命令说明需要执行核对，文档网站是维护源的派生物。它还区分用户说明、开发参考、提案和历史材料。

本地借鉴：按任务渐进读取、源文件先更新、未验证操作诚实标注。双语逐行配对、固定 Summary 长度、特定 YAML kind 与模板体系不搬入本仓。

### D6 — 按未来决策价值管理知识

[官方 dsh-archive-agent-notes](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/skills/dsh-archive-agent-notes/SKILL.md)按保留理由、替代方案、负向保证和未来误判风险处理笔记，不按年龄或字数执行配额；新增记录时检查同题材重叠。

本地借鉴：复用已有知识拥有者，保留有用的拒绝理由。本地 accepted Spec、Review/Conformance 证明的不可变性和替代边继续由本地 authority 决定；不照搬 Note 移动、改写或删除语义。

### D7 — 按实际变更选择证据

[官方 dsh-pre-push-checks](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/.agents/skills/dsh-pre-push-checks/SKILL.md)验证 live base 后选最小可信检查，区分测试选择与源覆盖；配置、动态调用及发布产物需要显式补充验证。未失效的证据不因随后 commit/push 就重复执行，广泛整合则需要更广覆盖。

本地借鉴：解释每个检查证明什么、为何重跑或不重跑；不引入其 pnpm 命令、100% 覆盖率常数、stack-sync 例外或宿主权限升级政策。

根 [AGENTS.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45fbc7f8e46dd73185e68295696d1297887/AGENTS.md)读取部分同时区分 pre-stable APIs 与已发布 Session generations，后者不得任意改写。这说明“敢于删除”必须与本仓真实兼容及数据承诺一起解释，而不是外部政策一键套用。

## 3. Hermes：成功方法与失败教训一起读取

### H1 — 官方大规模重构 PR

[PR #102117](https://github.com/NousResearch/hermes-agent/pull/102117)的说明覆盖职责抽取、共享 helper、dispatch table、薄公共入口、插件兼容、打包和文档同步。作者报告 source LOC 降低 34.4%，同时报告模块/导入边增加、部分入口 import 变慢和检索模拟的中位数反向变化。删除量不是单向收益证明。

PR 还描述外部插件仍引用旧导入路径，以及移动模块后 wheel 包含清单遗漏的修复。由此借鉴接口清单、真实制品 smoke 和派生文档对账；不是只看单测或静态“无人使用”。其按目录加载 Agent 指引的做法可降低无关上下文，但需要保留根部约束与路由完整性。

这些是 PR 作者报告的结果，本任务未运行 benchmark、未复验全套测试，也未审查数千文件的完整实现。“零行为变化”是作者的目标/表述，不作为本地已证实结论。

### H2 — 官方 1,393-agent 运行复盘

[Issue #103563](https://github.com/NousResearch/hermes-agent/issues/103563)明确分开历史运行、故障观察、模型/重放估计和修复后的 A/B。其已修订范围排除了部分 cache-routing 与 thinking-prefix 归因，不再主张整次运行的总节省；成本估算不是发票。

所读复盘报告过公开名称与测试遗漏、子任务结果摘要截断、失败通知延迟及认证并发问题。尤其需要区分提前发出的进度/失败通知和最终完整结果：提前通知不能吞掉最终结果的交付记录。

本地借鉴：候选先反证、外部接口单独查、worker 交付绑定完整产物与最终 HEAD、进度不代替完成、预算先试点。不同统计口径不能混算；1,393 是该运行的子任务统计，不是推荐同时启动的并发数。复盘中的历史收益与修复状态未在此独立复现。

### H3 — 当前 simplify-code Skill

[官方 simplify-code](https://github.com/NousResearch/hermes-agent/blob/77fb7f0a709b4df2c17822da3a08f8c93de3b3fb/skills/software-development/simplify-code/SKILL.md)用复用、质量、效率、altitude 四个视角检查最近变更，要求给出成本、置信度、风险和调用者证据，并保护有意的兼容或隔离层。没有委派工具时可顺序完成视角，不冒称运行了并行审查。

本地借鉴视角和“修到真实机制”的追问，但不采用固定四 Agent、风险标签自动授权、静默丢弃重要审查意见或每次编辑自动运行。低置信度候选保持未证实，风险分类不取代本仓三轴路由。

### H4 — 当前 dynamic-workflow Skill

[官方 dynamic-workflow](https://github.com/NousResearch/hermes-agent/blob/77fb7f0a709b4df2c17822da3a08f8c93de3b3fb/optional-skills/autonomous-ai-agents/dynamic-workflow/SKILL.md)先用确定性脚本组织材料，再向独立单元派发判断任务；共同 Brief、分域工作、小批试点、反证、每步提交与每轮整合共同约束过程。它特别提醒 worker 在整合后继续提交会使尾部工作遗失，以及单分支绿灯不能证明组合正确。

本地适配为隔离写入面、独占路径、最终 HEAD 停写确认、提交/内容对账和整合树验证。不同合并方式采用相应证明，不能一律用祖先计数。外部的共享索引/按行并写、固定并发数、一个全局测试 runner、无条件以 main 行为为准及专用后台任务语义均不照搬。

## 4. 本地去重和落地位置

| 本地拥有者 | 复用内容 | 此次不做什么 |
|---|---|---|
| Governance V1 | 授权、三轴、exact coordinates、证据范围、独立审查与停止 | 不新增 blocker 类型或固定审查角色 |
| Model Convergence V1 | 真实消费者、减法、桥接退出、非复活与历史保留 | 不原地扩大 accepted Contract |
| Operational Layer V1 | 窄任务入口、非权威知识和不越权的 Skill | 不宣称此次已实施整套 Skill/Record 分发 |
| PR #17 的仓库质量主题 | 文档/使用入口的方法背景 | 不把提案当 active authority，不改该 PR |
| main 中的 Release Recovery Assurance 提案 | 测试环境差异和分层验证的方法背景 | 其 `status: proposed` 不因 PR #18 合并就变成 accepted |

Operational Layer 的历史研究已记录 DeepSeek `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`。因此本次是新的固定版本对照与实操补充，不另造一个同义 governing Spec。实操指南只提供执行选择；新增强制义务或自动分发需要另按现有流程，不以参考资料偷渡。

## 5. 文件同一性记录

以下是 connector 返回的 Git blob 身份，可与固定提交中的文件核对；不是性能或实现正确性证明。

| 来源 | Git blob |
|---|---|
| D1 | `6ee736796c5ab961a3256a55d3109a65fcf0e490` |
| D2 | `7453e110ef66e48bdaab1719e07d894e4764e7f8` |
| D3 | `d9fd0f1700476f8fc9bb6f90f3824ce8a8304de6` |
| D4 | `bb8347823b99fb8c871c697032b2bf33d1bcea43` |
| D5 | `83eee5d526ef6f315fe67fa0f39b7780fe730484` |
| D6 | `a08e4b51797128bf76a7357165d72a382d056e84` |
| D7 | `6567dde5dc6df2d9d292fda3f6b8daac8b7dcd9a` |
| DeepSeek AGENTS.md（部分读取） | `ce14413b4cda2af567a7e2bbbf1932f6a734ecf7` |
| H3 | `0dcfae3084b22544c3d250f5265c5964325543eb` |
| H4 | `0955ba8acbc126129dd52adf46fb2e3a7c51a8fe` |

H1/H2 是可变讨论说明，不伪装成代码 blob；本文件保存读取后的概括及其限制。未取得博客全文、原始 run 数据库、完整遥测或完整 benchmark 数据；未重新验证全部关联 PR 的实现与运行效果。后续需要依赖这些材料作关键事实判断时，先取得相应原始材料或可复核快照，不能扩大本次证据范围。
