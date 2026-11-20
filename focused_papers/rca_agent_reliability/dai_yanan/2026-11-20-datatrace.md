---
title: "DataTrace: Benchmarking Data Agents for Evidence-Grounded Root-Cause Localization"
authors: ["Tung Sum Thomas Kwok", "Xiaotian Lin", "Yuyu Luo"]
year: 2026
publication: "arXiv"
publication_type: "preprint"
status: "preprint; KDD2027_acceptance_author_reported_unverified"
doi: ""
arxiv_id: "2611.18926"
url: "https://arxiv.org/abs/2611.18926"
pdf_url: "https://arxiv.org/pdf/2611.18926v1"
first_publication_date: "2026-11-13"
formal_publication_date: ""
last_updated: "2026-11-13"
version: "v1"
topics: ["Agent / LLM", "Evidence / Process Reliability"]
score: null
reading_priority: "medium"
full_text_reviewed: false
created_at: "2026-11-20"
reading_scope: "abstract_and_public_pages; selected_body_crosschecks"
canonical_file: "papers/2026/11/2026-11-20-datatrace.md"
focused_groups: ["liu_chuntai", "dai_yanan"]
---

# DataTrace: Benchmarking Data Agents for Evidence-Grounded Root-Cause Localization

## 1. 基本信息

作者与原始标识见元数据。发表状态：arXiv；preprint; KDD2027_acceptance_author_reported_unverified。首次公开与正式发表分开记录；空日期表示未核实，不以收录日期代替。论文链接：[v1 原始来源](https://arxiv.org/abs/2611.18926)；[原文 PDF](https://arxiv.org/pdf/2611.18926v1)。本次不保存大型 PDF。

## 2. 一句话总结

将数据管道根因命中与已查看支持证据的覆盖分开评价。 [v1 原始来源](https://arxiv.org/abs/2611.18926)

### 2.1 摘要中文翻译

范围：摘要要点译述，非逐句全文翻译；依据上述版本的公开摘要，不混入助手评价。

正确答案可能没有证据支持。DataTrace 通过故障注入构造根因与证据路径，并分别检查答案正确性和调查证据。 [v1 原始来源](https://arxiv.org/abs/2611.18926)

### 2.2 数据集—问题—解决方案

| 数据或场景 | 具体问题 | 方法 / 研究方案 | 验证边界 |
|---|---|---|---|
| 83 个可运行数据库 / 数据工件环境；场景不是微服务。 | 最终答案分数掩盖了 unsupported correct diagnoses。 | Typed artifact graphs、受控注入及 CoSE generator-solver 协议，由外部 verifier 检查可复现故障和证据。 | 原文报告，未独立复现；不能跨数据集横比分数 |

研究型基准 / 失效分析不必提出新检测算法；这里按实际贡献记录，不将作者的实证发现包装成解决所有问题的方法。[v1 原始来源](https://arxiv.org/abs/2611.18926)

## 3. 研究背景

本专题关注观测事实进入假设、调查决策与最终诊断的过程。下文区分作者方法和迁移到两份开题报告的助手建议，不把相近任务当作同一实验场景。

## 4. 研究问题

见 2.2 的具体问题。阅读时重点核对：作者改变了哪个环节、哪些条件固定，以及结论支持的是方法有效性、失败分类还是资源权衡。

## 5. 核心方法

### 5.1 整体框架

Typed artifact graphs、受控注入及 CoSE generator-solver 协议，由外部 verifier 检查可复现故障和证据。 [v1 原始来源](https://arxiv.org/abs/2611.18926)

### 5.2 关键模块

以原文方法名与阶段为准，模块作用参见 2.2；本次未独立核查每个实现细节，不能由摘要补出未说明的训练或调用流程。

### 5.3 数学公式

本次未逐项核查原文公式与理论假设，不添加未经核实的公式；后续精读时从原文标注式号补充。

### 5.4 数据输入与输出

输入场景见 2.2；阅读时区分原始观测、证据记录、候选判断和最终输出，不将离线真值作为可部署输入。

### 5.5 技术路线

重点追踪输入证据经过方法模块后，改变了诊断 / 回答、过程评价或停止中的哪一步；具体流程以原文而非本专题的迁移设想为准。

## 6. 创新点

- 作者主张：一句话总结及 2.2 描述的方法 / 分析贡献。
- 助手评价：与专题有关不等于构成新课题的创新性证明。应与最接近的工作固定任务、信息及预算做对照。

## 7. 实验设计

- 数据集 / 场景：见 2.2，保留原文版本和规模限定。
- Baseline、切分、预算、种子及消融：除本卡明确记录者外，本次未逐项核实，不能据摘要视为完全公平对比。
- 指标：关键结果使用原文名称；没有数值则保持定性，不补造指标。

## 8. 关键实验结果

摘要：七个专有模型平均根因准确率 48%，逐模型条件无依据率均值 18%；不要把不同分母混成总错误率。 依据：[v1 原始来源](https://arxiv.org/abs/2611.18926) 的摘要 / 官方概述；非独立重现实验结果。

## 9. 局限性

### 作者明确承认的局限性

本次未完整审阅局限性章节，不补写作者未明确承认的限制。

### 自己的分析

工件图中的证据路径与运行时 metrics / logs / traces 的解释关系不同，迁移须重新定义。

## 10. 与相关研究的联系

在专题中按证据组织、核验、错误定位、修正或停止比较，不能因都含 root cause 就忽略“系统故障根因”与“Agent 轨迹错误根因”的不同。具体候选见两类专题阅读索引。

## 11. 对研究的启发

以下是助手的迁移建议，不是论文已验证结论：

- 对刘春泰方向：评价证据误用时将“答对但无依据”单列。
- 对戴雅楠方向：避免直接把答案正确作为可停止标签；可借鉴证据覆盖对照。
- 可验证实验：固定案例、宿主模型、可见信息和调用预算，只替换拟借鉴模块；记录原始 / 修改后轨迹，分别评价任务正确性、过程依据和成本，并检查原本正确案例是否变坏。

## 12. 阅读建议

优先级：medium。先读根因与证据评分的分母，再看故障生成和核验。
是否值得复现：先确认数据、代码和目标任务匹配，再决定；本次没有运行代码或下载模型。

## 13. 总结可靠性

主要依据摘要、元数据、官方公开页及此前选读正文的核对，属于初步阅读笔记，未完成逐段全文精读、全表核查或复现。`full_text_reviewed=false`，score 留空。未知数据、超参数和消融不推测。访问日期：2026-11-20。

分类副本与正本使用同一标识；总索引只一行。正本路径：`papers/2026/11/2026-11-20-datatrace.md`。若需添加个人笔记，请另存 notes 文件，避免自动同步覆盖手改副本。

## 14. 参考来源

- [v1 原始来源](https://arxiv.org/abs/2611.18926)
- [原文 PDF](https://arxiv.org/pdf/2611.18926v1)
- 代码 / 数据入口：本次未独立核实可运行性，不写成已复现。
- 作者 comments 声称 KDD 2027 Datasets and Benchmarks 录用，本次未独立核实，仍按预印本。
