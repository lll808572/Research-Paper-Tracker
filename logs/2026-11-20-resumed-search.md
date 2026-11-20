# 2026-11-20 恢复检索

- Run ID：20261120-112815-resumed；类型 daily，用户要求恢复今天的周期研究。
- last_attempt_at：2026-11-20T11:28:15+08:00。
- 原成功截止：2026-11-18T17:01:22+08:00。
- 本次增量范围：2026-11-18T17:01:22+08:00 至 2026-11-20T11:28:15+08:00。
- 实际检索包含 24 小时重叠：2026-11-17T17:01:22+08:00 至本次开始；按原始提交或更新时间过滤，不按搜索页面抓取时间。
- 早间 08:27 失败记录保留，不能改写成成功；本次是新的运行记录。

## 运行前处理

用户明确授权提交两份 DOCX。提交 `4df7204` 已上传 origin/main，同时保存早间失败日志。随后 `git pull --ff-only origin main` 成功，开始写入研究文件前工作区干净。没有读取或将 DOCX 内容发送给检索服务。

## 检索来源和查询

发现：网页搜索，包括 arXiv、OpenReview 定向搜索；第三方镜像或聚合结果仅提供线索。
核实：四份候选的 arXiv 元数据和版本记录，两篇选中论文的部分 HTML 正文，以及 PACT 作者代码仓库。
未穷尽所有配置来源，未调用 Crossref / OpenAlex / Semantic Scholar API，没有运行实验。

共执行 12 条搜索查询；总命中数未知。以下为传给搜索工具的原始字符串，操作符是否严格生效由搜索服务决定，最终逐篇核对时间。

1. `site.arxiv.org "time series" "anomaly" after:2026-11-17 before:2026-11-21`
2. `site.arxiv.org "root cause" after:2026-11-17 before:2026-11-21`
3. `site.arxiv.org "agent" "forecasting" after:2026-11-17 before:2026-11-21`
4. `site.openreview.net "2026" "time series" "anomaly detection"`
5. `site.arxiv.org/abs "root cause" "19 Nov 2026"`
6. `site.arxiv.org/abs "time series" "19 Nov 2026"`
7. `site.arxiv.org/abs "agent" "18 Nov 2026" diagnosis`
8. `site.arxiv.org/abs "anomaly" "20 Nov 2026"`
9. `"When Normal-Only Updates Are Not Enough" github`
10. `"Recurrent Domain Incremental Adaptation" OpenReview`
11. `site.arxiv.org "root cause analysis" "Nov" "2026" "19"`
12. `site.arxiv.org "LLM agent" "time series" "November 2026"`

查询发生于本次开始至结束之间，未独立记录秒级时间。RCA / OpenReview 检索未得到更合适的窗口内核实对象；不因此断言没有相关新论文。旧期刊文章及新闻 / 软件发布未进入原始元数据核查候选数。

## 候选、去重及选择

计数口径：4 篇已打开 arXiv 元数据页的不同候选，按 arXiv ID / 标题与库内 2 篇核对，库内重复 0，候选重复移除 0，新收录 2，暂缓 2，更新旧卡 0。多次打开同一页面不重复计数。

| 候选 | 原始时间记录（UTC） | 决策 |
|---|---|---|
| [PACT，2611.24075](https://arxiv.org/abs/2611.24075) | v1 11-18 09:05:22 | 收录：变化工况下时序故障分类适配；作者仓库可查，但只提供 FD 最小复现范围；作者称在审，非录用 |
| [Normal-only TTA，2611.23761](https://arxiv.org/abs/2611.23761) | v1 11-18 03:14:49 | 收录：重叠窗口补发现；实验诊断贡献明确，与 PACT 对照适配条件，代码作者称发表后发布 |
| [Multi-Agent Memory Inconsistency，2611.22245](https://arxiv.org/abs/2611.22245) | v1 11-17 05:47:01；v2 11-18 06:42:29 | 暂缓：v2 在重叠窗口，证据传递问题很相关；本次优先形成工况适配的方法 / 失效分析组合，未比较版本不声称实质更新 |
| [AgentAbstain，2607.10059](https://arxiv.org/abs/2607.10059) | v1 07-11；v2 11-18 03:51:43 | 暂缓：近期版本更新非首次发布；未比较版本与独立核实聚合页所称 NeurIPS oral，不据此标为正式录用 |

两篇均非综述。PACT 是少标注固定类别分类适配，另一篇是重构式异常检测分析，不能互相比较分数。两篇 DOI 页面标 pending registration，未写入已注册 DOI；分数留空，不用未核实维度虚构精确评分。

## 产出与限制

- [PACT 卡片](../papers/2026/11/2026-11-20-pact.md)
- [Normal-only TTA 卡片](../papers/2026/11/2026-11-20-normal-only-tta.md)
- 更新三个索引和 search_history.md；模板包括摘要要点译述、数据集—问题—解决方案、原文 / 自己评价区分。
- 两篇均 `full_text_reviewed=false`；只阅读部分方法、实验、附录或限制，未逐段核对全部正文、证明和参考文献，未独立复现。
- 研究查询 / 正文访问失败：无。会议及 DOI 注册未知已披露；不等同于穷尽整个研究方向。
- Git 同步状态：pending（提交前记录）；以本次 Git 历史及回复中的实际推送结果为准，不能据此字段断言已经上传。
- 检查完成时间、最终研究状态及成功覆盖区间记录于 search_history.md 同 Run ID 小节。
