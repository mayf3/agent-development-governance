# 发布与恢复：作者桌面案例

```text
RECORD_KIND = NON_NORMATIVE_AUTHOR_SCENARIOS
BASE_HEAD = e123130562774cafb78bb212a9b54d7f10658c4f
RECORDED_AT = 2026-09-16
METHOD = text-based design counterexamples
INDEPENDENT_REVIEW = NOT_PERFORMED
PRODUCT_TESTS = NOT_RUN
PRODUCTION_READBACK = NOT_PERFORMED
```

[标准正文](../../specs/AGENT_RELEASE_RECOVERY_ASSURANCE_V1.md)；[来源摘录/限制](SOURCE_MAPPING.md)。以下是依据正文重新构造的去标识化情景及作者预期判断，不是附件中逐项执行的事实，也不证明未来实现符合标准。独立 Reviewer 应寻找可满足全文但违反目标的反例。

| Case | 输入 | 作者依据正文的预期判断 | 对应 |
|---|---|---|---|
| C01 | selftest 用新 payload，apply 用旧 payload，但源码 SHA 相同 | 拒绝安装组合；源码同一性不能证明产物一致 | CTR-RRA-002 / ACC-RRA-002 |
| C02 | CLI 与 runtime 独立版本，但组合受审且安装/加载身份相符 | 允许；不要求所有版本号或 ID 相等 | CTR-RRA-002 / ACC-RRA-002 |
| C03 | 两个部署入口各拿自己的锁，能改同一个 target | 不满足同一变更域协议；新 wrapper 成功不能证明竞争入口退出 | CTR-RRA-002/008 / ACC-RRA-002 |
| C04 | 校验通过后换配置或构建产物，沿用原 PASS | 不允许；需要匹配实际受审组合，关键前态在互斥后重读 | CTR-RRA-002 / ACC-RRA-002 |
| C05 | routing reader 的属组直接取 incident 目录属组 | 须有对象角色合同和双层读取证据，不能从偶然属组推导 | CTR-RRA-003 / ACC-RRA-003 |
| C06 | root 能 cat，实际 reader 过不了 OS 或应用 gate | 权限结论不通过；两个读取条件分别验证 | CTR-RRA-003 / ACC-RRA-003 |
| C07 | fixture 同一 UID/GID、no-op chown、清空 xattr，声称生产权限通过 | 只能证明未被消除的部分；关键风险仍未验证 | CTR-RRA-005 / ACC-RRA-003 |
| C08 | 宿主 shim 覆盖纯逻辑；目标平台隔离结果另证 metadata/加载语义 | 允许分层组合证据；不强制所有测试无 mock | CTR-RRA-003/005/006 / ACC-RRA-003 |
| C09 | 第一次失败后留有通知事实和 partial preimage，重试仍用原 receipt | 先核对实际前态和事务身份；不得重复副作用或假设空状态 | CTR-RRA-004 / ACC-RRA-004 |
| C10 | 回滚旧代码并清空 dedupe/执行账本，使测试绿灯 | 拒绝；回滚代码不能抹去需保留的业务事实 | CTR-RRA-004 / ACC-RRA-004 |
| C11 | 旧版本不能理解已经保留的新状态 | 不可将 rollback 报告安全；停止或走已有授权替代处置 | CTR-RRA-004 / ACC-RRA-004 |
| C12 | 业务结果 unknown，但该 turn 已有产品合同认可的精确终止证明 | 保持区分；不虚构成功、不自动重跑，也不强制常驻进程退出 | CTR-RRA-004/006 / ACC-RRA-004/005 |
| C13 | native no-op 成功，Router/真实 Agent/投递未测，却报整体恢复 | 拒绝整体声明；只确认对应调度路径 | CTR-RRA-006 / ACC-RRA-005 |
| C14 | 磁盘 target 更新，但运行进程仍加载旧 generation | 安装与加载分别记账，不能宣称运行闭环 | CTR-RRA-002/006 / ACC-RRA-002/005 |
| C15 | W2 另一个进程，但与 W1 共同依赖已损坏的 incident 状态 | 不能声称隔离该故障；验证实际报告路径，不新加第三个监控充数 | CTR-RRA-007 / ACC-RRA-006 |
| C16 | 兜底明确不覆盖某共享网络故障，且没有相反既有承诺 | 可以记录盲区；不能据此声称完全独立 | CTR-RRA-007 / ACC-RRA-006 |
| C17 | migration backups 仍在 loader/rollback 热路径，准备为整洁先删 | 拒绝；先证明当前模型保留必要事实并按已有收敛规则退出 | CTR-RRA-008 / ACC-RRA-001 |
| C18 | 实现违反已明确 reader 合同；另有任务遇到未定义 reader 角色 | 前者修实现/回归；后者只停止依赖缺口的推进并 re-PREFLIGHT | CTR-RRA-001/008 / ACC-RRA-001 |
| C19 | 小型无关文档修正，被要求全身份 census 和全发布矩阵 | 拒绝过度治理；没有触发相应表面 | CTR-RRA-001/009 / ACC-RRA-001/007 |
| C20 | 无权限取得关键环境结果，于是写 N/A；或擅自上生产补证据 | 两者都拒绝；保留未验证，只走允许的证据/授权渠道 | CTR-RRA-001/005/006 / ACC-RRA-003/008 |
| C21 | 只有 source Spec 合入；未分发的 docs 链接被声称已在消费者生效 | 拒绝；需自足分发、精确采用及实际 canary 证据 | CTR-RRA-009 / ACC-RRA-007/008 |
| C22 | 把报告目标“root-owned 代码/四边界”当成当前事实或通用强制布局 | 拒绝泛化；保留报告限定，具体产品语义仍本地决定 | CTR-RRA-001/009 / ACC-RRA-008 |

## 作者检查结论及限制

正文提供了上述反例的拒绝依据和合法多版本、有限 mock、有限隔离的正例边界。此表是文本自查，不是 22 次产品测试；机械引用覆盖也不能判断这些义务在未来实现中是否满足。独立审查、分发 canary 和实际产品运行验证均未由本记录完成。
