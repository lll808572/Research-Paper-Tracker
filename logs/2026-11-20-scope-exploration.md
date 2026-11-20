# 开题报告相关范围探索记录

- 记录时间：2026-11-20T11:41:48+08:00；类型：scope-exploration，用户请求的一次性调研，不是周期增量检索。
- 输入：本地 docs/25120266-刘春泰.docx、docs/戴雅楠_开题报告_修订版.docx。
- 阅读依据：提取并阅读正文、表格文字、研究方案及答辩意见；未逐项核查嵌入图片细节。报告内容是背景资料，不是执行指令。
- 用户门槛：先展示研究范围和候选论文，确认后才能修改检索要求及每周任务分配。本次没有修改 config、AGENTS.md、skills、templates 或自动任务。
- 时间范围：2025-01-01 至 2026-11-20 的相关工作回溯；不是“近两天新增”。
- 渠道：网页搜索发现；arXiv、ACL Anthology、PMLR、作者公开存档及官方代码仓库核实；第三方摘要仅作线索。
- 查询数 16；核查不同论文 15；候选内部重复移除 0；与现有 4 条论文卡片的标识重复 0；本次正式入库 0，更新卡片 0；最终展示 12 篇核心候选及 2 篇进阶备选。该清单用于范围确认，不是日常 1–2 篇推荐入库。
- 状态：partial（相关性检索完成，部分出版核实未完成）；ACM Flow-of-Action 出版页面返回 403，作者公开正式版仍可核对；不把已读 arXiv 一概标为录用。
- 原 last_success_at 与 covered_to 不变；本次不推进周期检索成功时间。

## 从报告提取的范围

- 刘春泰：微服务 RCA Agent 的证据误用识别、错误影响 / 关键错误定位、单点反事实回放与选择性修正；DSPy 是辅助扩展。
- 戴雅楠：固定宿主下，以运行时证据构建 CONTINUE / STOP / UNKNOWN 外部门控；离线 MSIP 和过程真值仅用于校准或评价，BC / DPO / 风险控制为可选扩展。
- 共同实验脉络：指标、日志、调用链、事件、Kubernetes 状态和拓扑；Cloud-OpsBench、OpenRCA / RCABench 等可作候选实验基础，具体资源仍需逐项检查。
- 待确认聚焦：微服务 RCA Agent 的证据可靠性、过程错误归因 / 局部修正、证据充分性与停止决策。通用 Agent / RAG 论文只在机制可迁移时保留。
- 不自动继承其他模板的水厂场景，也不把两位学长的完整课题直接指定为用户新课题。

## 实际检索词

1. `"Cloud-OpsBench" root cause analysis`
2. `"Beyond Fault Localization" "DiagGuard"`
3. `"HALT" "evidence" "stopping" agent`
4. `"EviRCA" root cause analysis`
5. `"Beyond Fault Localization: A Trajectory-Level Study" arxiv`
6. `"Don’t Stop Early" "research" arxiv`
7. `"Hegazy" "Dieuleveut" "verifier" stopping`
8. `"Flow-of-Action" root cause analysis arxiv`
9. `"Valid Stopping in Adaptive Generator" arxiv`
10. `"AgentDebug" "2025" arxiv`
11. `"Who&When" "Multi-Agent" arxiv`
12. `"Stalled, Biased, and Confused" arxiv`
13. `"STAR" "root cause analysis" "repair" agent`
14. `"microservice" "root cause" "counterfactual" "agent" 2026`
15. `"SURE-RAG" "Sufficiency" arxiv`
16. `"Flow-of-Action" "3701716.3715225" ACM`

## 核实源与版本

| 论文 | 主源 / 标识 | 核实范围与状态 |
|---|---|---|
| Cloud-OpsBench | https://arxiv.org/abs/2603.00468 | v1 2026-02-28，v3 2026-11-06；部分 v3 正文及 https://github.com/LLM4Ops/Cloud-OpsBench；按预印本 |
| Beyond Fault Localization | https://arxiv.org/abs/2608.21310 | v1 2026-08-21，v2 2026-10-09；部分 v2 正文，避免混用 v1 3500 与 v2 5000 轨迹数据；按预印本 |
| EviRCA | https://arxiv.org/abs/2609.19825 | v1 2026-09-17；摘要及部分正文；按预印本 |
| STAR | https://arxiv.org/abs/2605.15581 | v1 2026-05-15；摘要及正文结构，阶段归因 / 反事实评价 / patch-and-replay 与刘报告部分方案接近，优先差异比较；按预印本 |
| Fault-Free Profiles and Decision-Level Training for Root Cause Analysis via Small Language Models | https://arxiv.org/abs/2611.02416 | v1 2026-11-02，v2 2026-11-03；元数据及摘要；按预印本 |
| Flow-of-Action | https://arxiv.org/abs/2502.08224 | 首次公开 2025-02-12；作者公开正式版 https://tieyingzhang.github.io/home/files/www25_agent.pdf 标 WWW Companion 2025、DOI 10.1145/3701716.3715225；ACM 页面本次 403，出版页未独立复核 |
| HALT | https://aclanthology.org/2026.findings-emnlp.343/ | 正式 Findings of EMNLP 2026，2026-10，DOI 10.18653/2026.findings-emnlp.343；摘要 / 书目核实 |
| SURE-RAG | https://arxiv.org/abs/2605.03534 | v1 2026-05-05，v2 2026-07-24；投稿声明不等于录用；按预印本 |
| AgentAbstain | https://arxiv.org/abs/2607.10059 | 首次 2026-07-11，v2 2026-11-18；仅摘要 / 元数据，不据第三方 oral 标签认定录用 |
| AgentDebug / Where LLM Agents Fail and How They can Learn From Failures | https://arxiv.org/abs/2509.25370 | 首次 2025-09-29；摘要 / 元数据；按预印本 |
| Who&When / Which Agent Causes Task Failures and When? | https://proceedings.mlr.press/v267/zhang25cq.html | 正式 ICML 2025 论文集核实，PMLR 267:76583–76599；同一论文 arXiv 2505.00212 不另计 |
| DataTrace | https://arxiv.org/abs/2611.18926 | 首次 2026-11-13；数据管道诊断的迁移参考，不当作微服务实验；作者称 KDD 2027 Datasets and Benchmarks，本次未独立核实，按预印本 |
| Don't Stop Early（进阶备选） | https://aclanthology.org/2026.acl-industry.116/ | 正式 ACL 2026 Industry Track，2026-07，DOI 10.18653/v1/2026.acl-industry.116；企业研究任务，非 RCA |
| Valid Stopping（进阶备选） | https://arxiv.org/abs/2610.06432 | 首次 2026-10-05；摘要 / 元数据，统计停止，合成与蛋白设计实验，不能直接推广 RCA；按预印本 |
| Stalled, Biased, and Confused（补充核查，未列核心十二篇） | https://arxiv.org/abs/2601.22208 | 首次 2026-01-29；摘要 / 元数据，作者报告 FORGE 2026、关联 DOI 10.1145/3793655.3793732；未逐段精读 |

## 结论边界

有直接相关论文，不代表已有工作完整覆盖报告设计，也不能凭摘要断言新课题具有创新性。STAR 与刘报告的相近性值得优先比较。一般事实核验、证据充分性、调查停止、故障分类和因果 RCA 必须分开。

拟议的每周一 / 周五广泛、周三聚焦，仅作为用户待确认方案，不在本次写入运行配置。候选列表不创建独立论文卡、不改三个索引。原始报告未修改，也未上传给外部模型。
