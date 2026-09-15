# Repository quality: external reference selection

状态：作者的非权威来源说明；不是外部认证、消费者采用记录或完整合规矩阵。配套 [proposed Spec](../../specs/AGENT_REPOSITORY_QUALITY_V1.md)。官方来源于 2026-09-15 通过只读网页查阅，以下为作者概括，不复制完整外部标准。

## Sources and bounded mappings

| Source | 固定版本或查阅坐标 | 借鉴内容及本地映射 | 明确未引入的义务 |
|---|---|---|---|
| [GitHub: About the repository README file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | 未标独立规范版本；2026-09-15 查阅，About READMEs 小节 | 项目用途、入门、求助与维护入口；`CTR-RQ-003` | 不固定 README 字数、语言或完整模板；不把 GitHub 展示顺序变成本地目录约束 |
| [GitHub: About community profiles](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories) | 未标独立规范版本；2026-09-15 查阅 | 推荐社区文件和贡献/安全入口；`CTR-RQ-006`、`CTR-RQ-008` | 社区清单检查文件是否存在于支持位置，不证明内容真实；不强制全部模板、行为准则或社区运营承诺 |
| [OpenSSF Best Practices: Passing criteria](https://www.bestpractices.dev/en/criteria/0) | Passing Badge 页面；2026-09-15 查阅 | 选取 `documentation_basics`、`documentation_interface`、`build`、`test`、`test_policy`、`version_unique`、`release_notes`、`no_leaked_credentials` 等主题；`CTR-RQ-003` 至 `CTR-RQ-006` | 本地条款是有界改写，不等价于通过这些外部条目；不导入完整 badge 要求、固定漏洞响应时限、英语要求或全部安全控制 |
| [Diátaxis](https://diataxis.fr/) | 未标独立规范版本；2026-09-15 查阅，首页文档类型说明 | 教程、操作指南、参考、解释对应不同读者需求；`CTR-RQ-004` | 不要求四个目录、四篇文档、特定网站工具或全量搬迁 |
| [OSPS Baseline v2026.02.19](https://baseline.openssf.org/versions/2026-02-19) | 页面明确 Version 2026.02.19；2026-09-15 查阅 | 参考 `OSPS-DO-01.01`、`OSPS-DO-02.01`、`OSPS-GV-03.01`、`OSPS-DO-07.01`、`OSPS-SA-02.01`、`OSPS-VM-02.01`、`OSPS-BR-02.01`、`OSPS-BR-04.01`、`OSPS-BR-07.01` 的文档/发布主题；`CTR-RQ-003` 至 `CTR-RQ-006` | 这些条目跨成熟度等级，不能称为某一完整 level；不导入整套控制、分支设置、签名/SBOM、强制人工角色或未来版本 |
| [OSI: Open Source Definition](https://opensource.org/osd) | 定义 Version 1.9，文本标记 2007-03-22；页面修改日期与定义版本不同；2026-09-15 查阅 | 公开源码不等于获得开源许可；`CTR-RQ-006` 的声明边界 | 不替产品 Owner 选择许可，不提供第三方材料权属证明，不把此表当法律审查结论 |

## Local decisions versus references

`CTR-RQ-001` 的动作触发和本地采用、`CTR-RQ-002` 的职责可解释性、`CTR-RQ-004` 的权威/历史分离与同变更同步、`CTR-RQ-007` 的不浮动引用、`CTR-RQ-008` 的比例化证据、`CTR-RQ-009` 的分发接入是针对本仓治理场景的本地设计；不能冒充外部标准逐字要求。父治理规范仍拥有授权、独立审查、发布门和消费者采用语义。

本表映射仅表示设计来源，不表示外部条款已被完全满足；特定文件名、命令和目录依然由拥有它们的仓库决定。日期是查阅坐标，不声称是不可变网页快照。接受后的本地 Contract 字节和分发 commit 才决定执行规则；来源网页变化或失效不自动改变规则。

## Adoption and release boundary

这次只提出源仓标准；没有申请或获得任何 OpenSSF badge/OSPS level，也未评估任一消费者整仓合规。未来分发需按 `CTR-RQ-009` 提供消费者可取得的自足规则和来源说明，不将源仓 rationale 的路径作为隐藏依赖。

完整外部合规、签名发布、SBOM、社区治理、贡献者协议或新 CI 强制门均需依据具体需要另行处理；已有本地义务不因本表“未引入”而被取消。
