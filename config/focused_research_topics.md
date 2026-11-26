# 开题报告相关论文检索范围

这是周三精确检索的主要编辑入口。用户已于 2026-11-20 确认刘春泰与戴雅楠两条支线，2026-11-26 新增董泓方向。修改后保存并提交 Git，任务每次读取本文件；无需把关键词再复制到自动任务提示中。

## 1. 总体研究范围

微服务根因分析（Microservice Root Cause Analysis）Agent 的证据使用可靠性与调查过程控制。
数据场景包括 Metrics、Logs、Traces、Events、Kubernetes 状态和服务拓扑；重点是证据到假设、诊断决策之间的关系。只研究诊断，不自动执行生产故障处置。

## 2. 刘春泰方向：证据误用、错误归因与选择性修正

分类目录：`focused_papers/rca_agent_reliability/liu_chuntai/`。

重点问题：
- 时间 / 实体范围错配、证据语义误解、症状与根因混淆。
- 把工具失败、数据缺失、未观测到错误当作反证；共有症状被当作机制特异证据。
- 独立验证、诊断轨迹审计、关键错误定位、单点反事实干预。
- 选择性修正、patch-and-replay、局部状态及调查分支恢复；评价正确结果保持和回归风险。

英文关键词：`evidence misuse`, `evidence grounding`, `reasoning failure`, `failure attribution`, `counterfactual replay`, `selective correction`, `trace repair`, `diagnostic verification`, `claim-evidence alignment`。

查询组合示例：
- `("microservice" OR "cloud" OR "Kubernetes" OR "AIOps") "root cause analysis" ("agent" OR "LLM") ("evidence" OR "verification" OR "repair")`
- `"RCA agent" ("failure attribution" OR "counterfactual" OR "trace repair")`

## 3. 戴雅楠方向：证据充分性、停止与暂不可判定

分类目录：`focused_papers/rca_agent_reliability/dai_yanan/`。

重点问题：
- 证据覆盖、竞争假设区分、诊断链闭合、证据冲突与取证可行性。
- CONTINUE / STOP / UNKNOWN；premature completion、over-search、重复或低价值查询。
- 证据充分后的可靠停止与证据不足时的继续调查 / 暂不判断，避免简单增加拒答来降低错误。
- 独立门控、成本与诊断质量权衡、轨迹级回放及端到端评价。
- BC、DPO、Conformal Risk Control 仅在直接改善停止策略且具备校准条件时作为辅助，不泛搜所有训练论文。

英文关键词：`evidence sufficiency`, `verification-aware stopping`, `evidence coverage`, `agent stopping`, `abstention`, `selective prediction`, `premature termination`, `over-search`, `information gain`, `adaptive stopping`。

查询组合示例：
- `("microservice" OR "cloud" OR "AIOps") "root cause analysis" ("stopping" OR "abstention" OR "evidence sufficiency")`
- `("tool-using agent" OR "search agent") ("verification-aware stopping" OR "evidence coverage" OR "abstention")`

## 4. 纳入与排除规则

优先纳入：微服务 / 云原生 RCA + LLM Agent + 上述任一过程问题；基准和过程级评价研究也可纳入。
其次纳入：通用 Agent、RAG 或其他诊断领域中直接研究证据核验、停止、错误归因、局部修正的方法，但必须在卡片说明迁移到哪个 RCA 环节，以及场景和假设差异。
一般排除：只有预测或异常检测分数提升、无 Agent 证据过程贡献的论文；泛聊天 Agent、通用记忆架构、纯代码修复、泛强化学习或传统因果图算法，除非明确提供本专题所需的方法或基线。

仍遵循 config/paper_criteria.md 和 AGENTS.md 的真实性、日期、去重与质量标准。周三每人最多 1 篇、合计最多 3 篇，允许 0 篇；本次用户明确要求整理已确认的整批候选，属于一次性回溯入库，不改变日常数量上限。

## 5. 分类与维护

- 专题总入口 `focused_papers/rca_agent_reliability/README.md`，各人目录分别保留完整 Markdown 副本；共同相关论文可复制到两边，不算重复入库。
- 先更新正本，再运行 `python scripts/sync_focused_library.py`；更新对应目录的阅读索引，运行 `python scripts/sync_focused_library.py --check`。
- 若副本相对上次生成记录已被手动修改，同步脚本停止且不覆盖；人工笔记宜另存各目录的独立 notes 文件。
- 修改分类范围只影响后续筛选；不自动删除、移动历史论文。需调整已有归类时显式维护目录索引和 catalog，并保留人工内容。

## 6. 建议起步阅读

刘方向：Cloud-OpsBench → Beyond Fault Localization → EviRCA → STAR → Who&When / AgentDebug。
戴方向：Cloud-OpsBench → HALT → SURE-RAG → AgentAbstain；Don't Stop Early 和 Valid Stopping 属于进阶迁移参考。
这些是阅读优先级，不是必须完成清单，也不将任何尚待核实的创新点当作已成立结论。

## 专题存储规则（2026-11-22 修订）

专题论文仅保存在 focused_papers/rca_agent_reliability/ 下对应学长目录，不再在 papers/ 中保存；共同相关论文两边各一份。catalog.json 的 canonical 选择其中一份分类卡片，copies 仅列另一分类的副本；总 CSV 同一论文一行并指向 canonical。更新 canonical 后同步，手改副本冲突时停止，禁止覆盖个人笔记。普通非专题论文仍放 papers/YYYY/MM/。

## 7. 董泓方向：强耦合水系统的多尺度证据驱动 RCA Agent

来源：本地 docs/25120234-董泓.docx 的研究内容与技术路线，仅作为范围依据；报告中的论文效果和计划不视为已独立验证的事实。
分类目录：`focused_papers/rca_agent_reliability/dong_hong/`。

核心场景：SWaT / WADI，闭环控制、连续传感器与离散泵阀状态、攻击传播及物理过程耦合。研究报警后的辅助根因分析，而非自动控制处置。

重点检索：
- 多信号候选检索、弱变化根因保留、过程角色与证据测点选择，区分根因和传播症状。
- 分测点 / 自适应多尺度回溯窗口、变化起点与时延，工况条件正常参考；真实攻击起点不可用来替运行时选窗。
- 工艺知识 RAG、工具计算与 LLM 协作、检索与重排序分解、竞争假设、支持与反证、Top-k 根因排序。
- 证据出处核查、工具复算、物理约束 / SMT 一致性、受限回查；一致性不等于因果证明。
- 事件级 / 干预模式隔离评价、目标可观测性、Retrieval@K 与 Rerank@k、同候选 / 同可见数据 / 同预算比较。

英文关键词：`SWaT`, `WADI`, `water treatment`, `water distribution`, `industrial root cause analysis`, `AgentRCA`, `DecompRCA`, `sensor selection`, `adaptive diagnosis window`, `operating-condition reference`, `process knowledge`, `evidence verification`, `candidate retrieval`, `root cause reranking`。

查询组合示例：
- `(SWaT OR WADI OR "water treatment") ("root cause" OR "fault diagnosis") (agent OR LLM OR "evidence")`
- `"industrial root cause analysis" ("sensor selection" OR "adaptive window" OR "normal reference" OR "reranking")`
- `("process knowledge" OR "physical constraints") ("diagnostic agent" OR "root cause analysis")`

纳入规则补充：优先水系统 RCA Agent；工业 / 化工诊断 Agent 或明确解决上述指标选择、选窗、条件参考和根因排序子问题的数值方法也可纳入，但必须说明迁移环节与假设差异。此条为董方向对第4节通用排除规则的特定例外。只有异常检测分数提升、没有上述诊断贡献的工作不纳入。不泛搜所有 SMT、RAG、分类和时间序列方法。

## 8. 周三固定窗口与配额（2026-11-26，优先于旧规则）

周三 focused 固定检索执行时刻往前 7 天首次公开的新论文，不追溯上次成功截止，不额外重叠或补齐历史；仅更新版本、正式发表但早已公开的论文不计新论文。刘春泰、戴雅楠、董泓各最多 1 篇，允许各自 0 篇，合计最多 3 篇独立论文。同一篇可同时作为多人的唯一推荐并各存完整卡片，总 CSV 仍一行；每人的新增推荐不超过 1 篇，不为凑数放宽质量。general 仍每次最多 2 篇，保持原增量规则。失败窗口记失败或部分完成，不推进成功记录；下一次 focused 仍只查当时最近 7 天，历史补检须另行请求。
