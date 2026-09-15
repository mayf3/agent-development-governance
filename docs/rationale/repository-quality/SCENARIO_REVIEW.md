# Repository quality: author scenario review

```text
STANDARD = AGENT_REPOSITORY_QUALITY_V1 (proposed)
AUTHORING_BASE = 9dcd0c49a5932e44e2801317b6281bdc6a168d25
REVIEW_KIND = AUTHOR_DESK_CHECK
OBSERVED_AT = 2026-09-15
INDEPENDENT_REVIEW = NOT_PERFORMED
PRODUCT_BUILD_OR_RUNTIME_TESTS = NOT_PERFORMED
DISTRIBUTION_OR_CONSUMER_CONFORMANCE = NOT_EVALUATED
```

本记录是作者按 [候选条款](../../specs/AGENT_REPOSITORY_QUALITY_V1.md) 逐项作出的桌面判断，不是可执行产品测试或独立审查。除案例 04 的两个源文件文本外，均为构造输入；未改变仓库可见性、发布制品、发送安全报告、使用真实秘密或操作生产。最终候选 commit 由 PR 绑定。

## Positive and negative cases

| Case | 输入 | 作者判断及最小闭合方式 | 对应条款 |
|---|---|---|---|
| 01 | 私有内部小工具改一个计算错误，没有公开或发行动作 | 只检查本次代码、必要测试与受影响说明；不能因未选开源许可而阻断，也不能据此宣称整仓通过 | `CTR-RQ-001`、`CTR-RQ-008` |
| 02 | 单文件工具已用 README 一段说明用途、入口和验证 | 可以满足结构要求，不为目录外观强拆多层；真实输入/输出仍须准确 | `CTR-RQ-002` |
| 03 | 多模块服务新增一个绕过已声明模块边界的直接依赖 | 不能因目录整齐而通过；说明归属并修正边界冲突，必要时走原有 authority 路由 | `CTR-RQ-002` |
| 04 | 同一基线 README 写 bootstrap superseded，CONTRIBUTING 写 proposed | 存在性检查不充分；作为文档一致性反例成立。此提案不改两份原文，后续试点按有效权威修正当前说明 | `CTR-RQ-003`、`CTR-RQ-004` |
| 05 | README 把只有 proposed Spec 或 mock demo 的功能写成已经支持 | 不能通过；区分计划/实验/已验证能力，不用新的文字掩盖实现违约 | `CTR-RQ-003`、`CTR-RQ-008` |
| 06 | 配置键已变更，旧快速开始、生成参考或译文仍使用旧键 | 相关交付未完成；同步维护源和适用文档；外部文档绑定配套版本并在发布前验证，不强改无关页面 | `CTR-RQ-004` |
| 07 | 为消除文档冲突，直接重写 accepted Spec 的历史语义或删除执行收据 | 不允许；使用当前状态说明/合法替代路径，保留权威与证据语义 | `CTR-RQ-004` |
| 08 | 快速开始依赖作者 HOME 私有脚本，但没有说明 | 不足以证明可执行；声明或消除隐含依赖，在干净环境重新运行并记录结果 | `CTR-RQ-005` |
| 09 | 项目明确依赖私人服务，仅本地 mock 能运行 | 可以记录本地已验证子集；真实集成保持未验证，不能以 N/A 或 mock PASS 宣称已承诺能力/完整发布验证完成 | `CTR-RQ-005`、`CTR-RQ-008` |
| 10 | 文档/治理仓库没有编译目标，但有内容检查和分发示例 | 用其实际交付物验证；不能因没有编译器判失败，也不能只数文件便声称示例可用 | `CTR-RQ-005` |
| 11 | 将含历史的仓库首次公开，工作树无秘密但旧 ref 存在合成秘密标记 | 公开门仍触发；检查实际将暴露的 ref/历史及附件，未完成前不声明就绪；不得自动重写历史或轮换凭据 | `CTR-RQ-001`、`CTR-RQ-006` |
| 12 | 公开发行标成 demo，LICENSE 随便复制、安全邮箱不存在、制品不是记录的源码版本 | 名称不取消责任；相关公开/发布不就绪。核对有权许可、真实渠道、commit/制品关系；不为补材料虚构权限或 SLA | `CTR-RQ-001`、`CTR-RQ-006` |
| 13 | 仅首次公开源码，没有任何版本化制品 | 许可、公开内容和报告入口仍适用；发行制品映射可说明无该对象，不能虚构版本或绕过其他公开检查 | `CTR-RQ-006` |
| 14 | 外部 OpenSSF 页面新增规定或链接失效 | 本地 Contract 不变；需要扩充时重新本地审查，不凭网页现场制造 blocker 或宣称 badge 达标 | `CTR-RQ-007` |
| 15 | 无关旧文档债务存在，但当次有界修复没有影响它 | 本次可按受影响范围完成；债务仍保留，不宣称整仓合规。首次公开/发行不能套用局部检查逃避适用完整矩阵 | `CTR-RQ-008` |
| 16 | 只创建 Spec/来源表，或消费者模板链接到不存在的源仓 docs 路径 | 不算分发启用；须有已接受基线、入口接入、版本/manifest、vendor 验证和两个真实试点。普通任务不能因此新增审批平台 | `CTR-RQ-009` |

## Directly inspected counterexample

案例 04 的原始文本来自以下同一 commit 的文件：

- [README.md L18-L29](https://github.com/mayf3/agent-development-governance/blob/9dcd0c49a5932e44e2801317b6281bdc6a168d25/README.md#L18-L29)，blob `44c8fe36e93f0c2436acf8861bd5f2bbdabb7f5b`。
- [CONTRIBUTING.md L12](https://github.com/mayf3/agent-development-governance/blob/9dcd0c49a5932e44e2801317b6281bdc6a168d25/CONTRIBUTING.md#L12)，blob `734aff522cba3f28f2faebb019264ced9aabb0b6`。

该对照只支持“文本存在矛盾”，不证明实际发布状态、普遍发生频率或本标准有效性。未执行真实代码仓库试点、敏感扫描或 vendor round trip；这些留给接受后的实施阶段，不能由本表替代。

## Author disposition

作者认为上述 16 个场景在候选条款中有明确处理边界；这是可供独立 Reviewer 反驳的自查判断，不是独立 PASS。尤其应审查普通范围与公开范围的切换、N/A 是否被滥用、受限验证是否夸大，以及未来分发是否能自足。
