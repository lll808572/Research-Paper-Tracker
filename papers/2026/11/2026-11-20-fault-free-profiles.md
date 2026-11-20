---
title: "Fault-Free Profiles and Decision-Level Training for Root Cause Analysis via Small Language Models"
authors: ["Kyoohyun Lee", "Woohyeok Park", "Taeyoon Kim", "Sungyong Baik", "Kyungyong Lee"]
year: 2026
publication: "arXiv"
publication_type: "preprint"
status: "preprint; venue_unverified"
doi: ""
arxiv_id: "2611.02416"
url: "https://arxiv.org/abs/2611.02416"
pdf_url: "https://arxiv.org/pdf/2611.02416v2"
first_publication_date: "2026-11-02"
formal_publication_date: ""
last_updated: "2026-11-03"
version: "v2"
topics: ["Agent / LLM", "Root Cause Analysis"]
score: null
reading_priority: "high"
full_text_reviewed: false
created_at: "2026-11-20"
reading_scope: "abstract_and_public_pages; selected_body_crosschecks"
canonical_file: "papers/2026/11/2026-11-20-fault-free-profiles.md"
focused_groups: ["liu_chuntai"]
---

# Fault-Free Profiles and Decision-Level Training for Root Cause Analysis via Small Language Models

## 1. 基本信息

作者与原始标识见元数据。发表状态：arXiv；preprint; venue_unverified。首次公开与正式发表分开记录；空日期表示未核实，不以收录日期代替。论文链接：[v2 原始来源](https://arxiv.org/abs/2611.02416)；[原文 PDF](https://arxiv.org/pdf/2611.02416v2)。本次不保存大型 PDF。

## 2. 一句话总结

用正常时期信号频率辅助判读异常，并对根因选择偏差做决策层纠正。 [v2 原始来源](https://arxiv.org/abs/2611.02416)

### 2.1 摘要中文翻译

范围：摘要要点译述，非逐句全文翻译；依据上述版本的公开摘要，不混入助手评价。

模型即使分析过传播关系，最终仍可能偏向最大的异常分数。作者用正常历史频率和决策偏好优化改善这一偏差。 [v2 原始来源](https://arxiv.org/abs/2611.02416)

### 2.2 数据集—问题—解决方案

| 数据或场景 | 具体问题 | 方法 / 研究方案 | 验证边界 |
|---|---|---|---|
| 四个 RCA 数据集；摘要明确提及 OpenRCA 的 Bank 场景，其余名称和完整设置待全文逐项核对。 | 常见正常波动可能被误当根因证据，最终选择也可能与已有分析不一致。 | Historical Frequency Profiling 描述正常期异常标记频率；Biased-Decision Correction 用同一分析后的分歧决策构造偏好。 | 原文报告，未独立复现；不能跨数据集横比分数 |

研究型基准 / 失效分析不必提出新检测算法；这里按实际贡献记录，不将作者的实证发现包装成解决所有问题的方法。[v2 原始来源](https://arxiv.org/abs/2611.02416)

## 3. 研究背景

本专题关注观测事实进入假设、调查决策与最终诊断的过程。下文区分作者方法和迁移到两份开题报告的助手建议，不把相近任务当作同一实验场景。

## 4. 研究问题

见 2.2 的具体问题。阅读时重点核对：作者改变了哪个环节、哪些条件固定，以及结论支持的是方法有效性、失败分类还是资源权衡。

## 5. 核心方法

### 5.1 整体框架

Historical Frequency Profiling 描述正常期异常标记频率；Biased-Decision Correction 用同一分析后的分歧决策构造偏好。 [v2 原始来源](https://arxiv.org/abs/2611.02416)

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

v2 摘要：4B 系统在 Bank 为 48.7%，OpsAgent 为 18.5%；只视为论文报告，不据摘要推断调用预算完全一致。 依据：[v2 原始来源](https://arxiv.org/abs/2611.02416) 的摘要 / 官方概述；非独立重现实验结果。

## 9. 局限性

### 作者明确承认的局限性

本次未完整审阅局限性章节，不补写作者未明确承认的限制。

### 自己的分析

偏好数据、正常历史窗口及平均多次采样协议需要仔细核对，不能简单推断小模型普遍优于大模型。

## 10. 与相关研究的联系

在专题中按证据组织、核验、错误定位、修正或停止比较，不能因都含 root cause 就忽略“系统故障根因”与“Agent 轨迹错误根因”的不同。具体候选见两类专题阅读索引。

## 11. 对研究的启发

以下是助手的迁移建议，不是论文已验证结论：

- 对刘春泰方向：适合研究共有症状与机制特异证据的区分，以及分析正确但决策错误。
- 对戴雅楠方向：不是显式停止方法，本次不作为停止主题必读。
- 可验证实验：固定案例、宿主模型、可见信息和调用预算，只替换拟借鉴模块；记录原始 / 修改后轨迹，分别评价任务正确性、过程依据和成本，并检查原本正确案例是否变坏。

## 12. 阅读建议

优先级：high。优先核对正常历史定义、偏好构造和评估采样协议。
是否值得复现：先确认数据、代码和目标任务匹配，再决定；本次没有运行代码或下载模型。

## 13. 总结可靠性

主要依据摘要、元数据、官方公开页及此前选读正文的核对，属于初步阅读笔记，未完成逐段全文精读、全表核查或复现。`full_text_reviewed=false`，score 留空。未知数据、超参数和消融不推测。访问日期：2026-11-20。

分类副本与正本使用同一标识；总索引只一行。正本路径：`papers/2026/11/2026-11-20-fault-free-profiles.md`。若需添加个人笔记，请另存 notes 文件，避免自动同步覆盖手改副本。

## 14. 参考来源

- [v2 原始来源](https://arxiv.org/abs/2611.02416)
- [原文 PDF](https://arxiv.org/pdf/2611.02416v2)
- 代码 / 数据入口：本次未独立核实可运行性，不写成已复现。
