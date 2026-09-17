# 发布与恢复：来源摘录、分类与本地映射

状态：非权威的来源快照与设计说明，不是生产审计或独立验收。
配套 [proposed Spec](../../specs/AGENT_RELEASE_RECOVERY_ASSURANCE_V1.md) 与 [作者案例](SCENARIO_REVIEW.md)。

## 输入身份与限制

- 原件：用户在 2026-09-16 提供的“粘贴的 markdown (1)。md(20260916-141928)”，586 行、30,495 字节。
- 原始 UTF-8 文件 SHA-256：`138bc81db3fa162768d0db3648db6dbee7a0e1223746983c034cf76a7af50bb3`。
- 下列 fenced blocks 逐字保留选定连续行；只在块外添加标题、原行号和解释。未修正文中 Markdown 转义；每块从实际上传文件提取，而非从聊天总结重建。
- 这些摘录随本 PR 的 Git commit 固定，Reviewer 可以直接读取其内容；完整原件的 hash 仅用于同一性核对，不能用 hash 代替未提供内容。
- 未把原件中 sandbox 链接指向的完整审计和 JSON 当作已取得资料；没有核验其中全部 24 个组件的九字段表或 24 条完整债务字段。
- “报告称”“历史记录”和“目标建议”保持区分。本任务未独立重现 Scheduler 故障，未读取当前生产，未验证修复或测量事故下降。
- 新标准的 MUST 是 Owner 请求下提出的本地设计选择；附件、下列映射和作者案例均不能自行成为 Product Authority。

## 摘录与对应

### S1 — 审计范围与未验证项

原件 L10–L24；摘录 UTF-8 SHA-256 `cf4f4a3ca59d15a931eb019398a46b737e72545ea8e1a1319f7dc3231d820dc8`。

````text
```text
INITIAL_REMOTE_MAIN =
104e2d5fe16f72290728be357453d93fb5b83394

FINAL_REMOTE_MAIN_READBACK =
1a1e59b8e41901c57beb8e5306a557350f56bfa9

AUDIT_MODE = READ_ONLY
REPOSITORY_MUTATION = NO
PRODUCTION_MUTATION = NO
LIVE_PRODUCTION_READBACK = NOT_PERFORMED
TESTS_EXECUTED_BY_AUDITOR = NO
```

收尾时 main 前进一个提交；已读取该提交完整 diff，变化限于 workflow 的 `currentExecutorType` 透传及测试，不改变下面的 Scheduler／部署结论。源码分析主要绑定实际读取的 `104e2d5`，没有把后续 handoff 中的候选修复混算成 main 已有能力。
````

分类与限制：这是附件自报的只读范围与源码坐标；本次没有独立重新审计该产品源码，也没有运行生产检查。

本地提案映射：OBS-RRA-002；ACC-RRA-008。

### S2 — 发布对象不相同，但绑定关系不能靠人工拼接

原件 L200–L212；摘录 UTF-8 SHA-256 `df3e25078a21a8fa8e4138e9faf5110ffad2fac1e4c9e0c66190406477363b8c`。

````text
这些标识并非全部多余：源码、配置、运行状态本来就不是同一种对象。问题在于，**它们没有统一归属于一份发布清单，很多关系需要靠脚本常量、目录名和 handoff 手动维持**。

历史记录还明确出现过：selftest 使用 `SOURCE_SHA`，真实 apply 使用旧 `WATCHDOG_PAYLOAD_SHA`。后来通过“先提交 payload，再提交 controller pin”修正，但这只是修复了该绑定，不等于整体发布模型已经收敛。

### 3. 同一 Scheduler 的入口语义已部分统一，安装来源却没有统一

CLI 与 broker 共享控制操作是已有的正向收敛；但 CLI 又构建自己的依赖闭包、复制依赖、建立独立 generation、切换独立 symlink。

因此：

> **同一份业务代码，不等于同一个实际运行版本。**

再叠加 HOME 默认路径、显式 `--store`、环境变量和尚待退役的旧域，就需要不断证明“这个入口到底在读哪个库”。
````

分类与限制：原文区分标识的合理差异和发布归属缺口，并将 selftest/apply 不一致明确称为历史记录。通用发布组成与产物验证义务是本地提案，不是报告已实现的目标。

本地提案映射：CTR-RRA-002；ACC-RRA-002。

### S3 — ownership 角色与两层读取条件

原件 L162–L168；摘录 UTF-8 SHA-256 `8fa56772a005fb11b7ec97e90e3bb9ff7ca3b6b2379a818119df955e3a9d7043`。

````text
这里混在一起的是四种不同角色：

```text
创建临时工件的人
控制部署回执的人
拥有运行状态的人
需要读取发布配置的人
````

原件 L179–L181；摘录 UTF-8 SHA-256 `a746332cccbe9a4edcfb6f8251aedfd93552e3cc78d3730af58da11f61165613`。

````text
这是**历史生产报告**，不是本次 fresh `stat`；但 main 中仍存在的参数和模板结构，独立支持“ownership 模型碎片化”的判断。

**目标不是再增加一个 GID mapper，而是只保留一份按对象角色定义的 ownership contract。**
````

原件 L339–L350；摘录 UTF-8 SHA-256 `3506d715e4077c4838d23f094c22bb0fb5cd9fa0b4df6cc9d6ed4f4f33b14750`。

````text
### SC-3：ownership 与平台协议碎片化

“文件可读”至少有两层：

```text
操作系统实际允许读取
应用安全校验接受这个 UID/GID/mode/path
```

root 能物理读取，并不代表通过 routing manifest 的 metadata gate。反过来，配置声明某 reader 合法，也不代表目录权限允许它读。

多个模块分别处理这些规则，再分别实现 ACL、xattr、readlink、copy、restore，就会出现“修 reader 后 installer 不接受；修 installer 后 backup 不接受”的连锁。
````

分类与限制：四角色与 OS/应用两层边界保留；不复制具体生产 UID/GID，也不将 root owner 目标当作通用事实。

本地提案映射：CTR-RRA-003；ACC-RRA-003。

### S4 — 失败后的实际前态会改变

原件 L124–L126；摘录 UTF-8 SHA-256 `7ad686b6797f5bf36739c1c7c2abaae37bcb7eee8030961869aa2e66d9eea224`。

````text
失败：
    按 phase / receipt 恢复代码、配置、plist、CLI、服务状态
    但不能回退 occurrence/fence 或已发生的通知事实
````

原件 L319–L335；摘录 UTF-8 SHA-256 `c4ae0c37b8dd98467790703dea0ba2cd527eff272b5bc4eedc994cc4b6598e2b`。

````text
### SC-2：真实 production preimage 没有完整成为输入模型

安装前态不仅是“旧文件内容”，还包括：

```text
旧 UID/GID/mode
ACL/xattr
物理路径与 symlink
dangling link
不完整 preimage
已经提交的 migration
已接受的通知
当前 loaded services
上次失败的 receipt generation
```

更重要的是，**一次失败后的生产前态可能已经改变**。因为 rollback 有义务保留 incident、通知及执行事实，不可能把所有东西都恢复成测试中的空目录。历史失败记录正是在这些维度之间轮流暴露问题。
````

分类与限制：报告中的保留义务有产品语境；本地规则要求拥有者划分可回滚状态与不可抹除事实，不要求其他产品创建同名 ledger。

本地提案映射：CTR-RRA-004；ACC-RRA-004。

### S5 — FIXTURE_ERASES_PRODUCTION_DIMENSIONS

原件 L366–L381；摘录 UTF-8 SHA-256 `6b427d3148261a0cb991d7a1166eebda2e5202f9df3d77751212bf9743176f2d`。

````text
### SC-5：测试保留了部分旧状态，却抹平了最危险的差异

不能说“没有测试历史场景”。总装 selftest 已经包含旧文件、partial preimage、重复执行和前像保留。

但它同时：

```text
把多个角色设成同一 UID/GID
将部分 chown 操作替换为空操作
以 shim 模拟 launchd
以空 legacy incidents/evidence/facts 起步
```

desired-state 测试也主要使用同一进程 owner/group，预先清理 xattr。这能证明部分逻辑，却不能证明真实多身份读取与安装链。

\*\*对应判断：\*\*与其叫 `FIXTURE_TOO_CLEAN`，更准确的是 **`FIXTURE_ERASES_PRODUCTION_DIMENSIONS`**。
````

分类与限制：保留“测试已有部分历史覆盖”的限定，不改写成“没有测试”；新增要求是结论必须限定在真实保留或有效证明的维度。

本地提案映射：CTR-RRA-005；ACC-RRA-003/004。

### S6 — 必要模型区分和 native canary 的覆盖

原件 L131–L146；摘录 UTF-8 SHA-256 `c34e91f4c769c4fbc6a1d09d50a6ad60a2ee673550904442193a6b8afe441e7f`。

````text
### 3. 哪些模型必须区分，不能为了“简单”合并

| 必须区分原因                                                    |                               |
| --------------------------------------------------------- | ----------------------------- |
| Job、Occurrence、Run、Session、常驻子进程                          | 定义、一次执行、执行证据、会话和承载进程不是同一个生命周期 |
| 业务 `outcome_unknown` 与终止证明                                | 能证明执行停止，不代表知道业务成功或失败          |
| 执行结果与 delivery 结果                                         | 答案生成成功、发送失败，不应重新执行业务          |
| Desired 与 observed                                        | 期望必须独立存在，才能发现 Job 丢失、被禁用或发生漂移 |
| 业务投递、Job failure 告警、Scheduler 运维告警                        | 三者的目标选择和授权来源不同                |
| Release、Runtime epoch、Store revision、Migration checkpoint | 发布版本、进程时代、数据版本和迁移来源不同         |

尤其要保留：

> **业务结果仍然 unknown，但该 turn 已有可信、精确终止证明**，是合法状态。它可以按合同释放对应执行 fence，但不能自动重跑旧 occurrence，也不要求常驻 child 整体退出。

这部分是不确定执行与不可逆副作用带来的**必要复杂度**。后面的减法不能破坏它。
````

原件 L542–L544；摘录 UTF-8 SHA-256 `5372f058142a5a2a2b4e055f02192f16641cb66e88806b1614321d6f43afc3a8`。

````text
### 一个必须单独保留的验收边界

当前 native canary 故意不进入 Router、AgentProcess、工具、凭据和投递；它证明的是 Scheduler 的安全 no-op 调度路径。部署后 finalizer 还检查 unrelated natural execution、quarantine 隔离和 durable dedupe，但仍不能把 native canary 的 PASS 单独翻译成“真实 Agent 与飞书投递已全部恢复”。
````

分类与限制：unknown、termination、delivery 和常驻进程的区分属于报告原意。这里只要求遵守各产品实际合同，不重新设计 Router/Scheduler 协议。

本地提案映射：CTR-RRA-004/006；ACC-RRA-004/005。

### S7 — 兜底共享故障面

原件 L413–L417；摘录 UTF-8 SHA-256 `a5ecf9f21d32eb8007656c14119ac9a3ec3a9581af0b199edb9ea4d62f3c6af6`。

````text
### 2. W2 需要真正缩小，而不是再复制一份 W1

当前 W2 检查的是 W1 心跳，但告警路径仍共用 incident、routing 等组件。因此它只能隔离部分故障，不能覆盖共同依赖损坏。

目标是：\*\*W1 的业务状态或软件坏了，W2 仍能用极小、独立路径报告“W1 不可用”。\*\*不需要让 W2 理解 occurrence、legacy fingerprint、migration backups 和完整业务 outbox。当前共享依赖可以从 runner 与 incident 模块看到。
````

分类与限制：原文先描述共享依赖，再提出 W2 目标；本地提案是对独立性声明给出故障集合与验证，不要求新增 W2 或第三个 watchdog。

本地提案映射：CTR-RRA-007；ACC-RRA-006。

### S8 — 迁移热依赖与旧入口退出

原件 L214–L228；摘录 UTF-8 SHA-256 `d772d2b8011ccc76179c870e34cffb9c6ac9e538c969896dde108467a49fb326`。

````text
### 4. 一次迁移没有结束，反而成为正常运行的依赖

这是本次最值得单独处理的债：

`loadIncidentState()` 和 `commitIncidentState()` 会验证 migration authority，继续读取三个 hash 命名的旧来源备份：

```text
legacy state backup
legacy evidence backup
migration facts backup
```

也就是说，旧材料不仅是审计存档，**仍是当前 incident 状态能否加载、提交的运行前提**。备份缺失、权限漂移或校验失败，都可能影响今天的 incident/health 路径。

不能现在直接删除这些备份。正确方向是：完成可信 checkpoint，使正常运行只依赖规范化后的状态；原始材料转为只读历史证据。
````

原件 L481–L497；摘录 UTF-8 SHA-256 `48ddd1aae8e9a641d21959aa28189e684533b743911be0670548c73aeca79624`。

````text
关键变化不是新加一个总 wrapper，而是：

**同一产物接受测试和安装；CLI 与 runtime 使用同一 release；普通部署不做历史业务纳管；迁移是明确的一次性操作；旧 apply 入口真正退出。**

### 6. 哪些应该删除

| 删除对象前提                           |                                     |
| -------------------------------- | ----------------------------------- |
| 多余 production domains／stores     | 全消费者与任务完成 disposition；重启／恢复不会复活     |
| 旧整树／Goal overlay／临时 Phase-2 竞争入口 | 唯一 controller 覆盖合法发布与恢复             |
| 独立 CLI 依赖 generation             | CLI 与 runtime 同 release，回滚同步        |
| 历史 Job 前缀匹配与日常 backfill          | 一次性纳管完成，desired 独立管理                |
| incident legacy migration 热路径    | 新 checkpoint 保留 dedupe、episode、送达事实 |
| 正常运行中的旧 schema upgrader          | 活跃旧数据退出、兼容回滚窗口结束                    |
| 无消费者的旧 flags／exports             | 调用者迁移完成，旧输入明确拒绝                     |

\*\*不得把“新 wrapper 调用所有旧脚本成功”当成收敛完成。\*\*那仍然要求未来维护者理解新模型、旧模型和中间映射。
````

分类与限制：这部分复用已 accepted 的历史模型收敛规则；checkpoint 和普通部署结构的具体选择留在产品仓，不能先删备份。

本地提案映射：CTR-RRA-008；ACC-RRA-001。

## 既有内容复用与拒绝泛化

已接受的 `AGENT_MODEL_CONVERGENCE_V1@e123130562774cafb78bb212a9b54d7f10658c4f` 已覆盖事实拥有者、桥接退出和恢复不复活。本次仅加入迁移热依赖/竞争入口的场景，不改写该规范，也不宣称其分发已经完成。

PR #17 的仓库质量提案仍单独处理职责说明、文档与开源发布；本 PR 不引用它作为权威，不修改其分支，不将其作为新标准接受/实施的前置依赖。

报告中的“四个运维边界”、六类对象、root-owned 代码、一份 manifest/journal、具体 checkpoint 与全套迁移顺序均不升级为所有仓库的架构。通用要求约束发布关系与事实，不约束物理文件个数或所有组件共用一个版本号。

报告原件 L288–297 明确区分 generation、review、真实 apply 和 closure；本提案不宣称已证实九次生产失败。原件 L394 将精确 review 视为结构成本放大器，本地取舍是减少需要绑定的对象，不通过取消审查隐藏失败。
