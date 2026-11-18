# 项目研究技能说明

## 本次恢复的进度

2026-11-18 已阅读《聊天记录.docx》及现有项目配置。历史回复作为背景资料；当前任务是准备研究技能，未执行论文检索、设置定时任务或上传本次变更。

## 已选工具

| 技能 | 用途 | 来源与处理 |
|---|---|---|
| deep-research | 文献比较、研究空白、研究问题 | 从本机 academic-research-agent-workspace 原样复制 |
| academic-paper-reviewer | 检查方法、实验、可复现性和局限 | 从同一工作区原样复制 |
| paper-tracker-daily | 每日检索、去重、卡片、索引和日志 | 为本项目编写 |
| paper-tracker-weekly | 每周技术路线比较和研究综述 | 为本项目编写 |

未复制 academic-paper、academic-pipeline：它们侧重写论文和投稿全流程，当前追踪任务不需要。未整体复制 academic-research-skills-codex-main：其 academic-research-suite 依赖同包 ars/、codex/ 等大量资源，仅复制入口不能独立运行；适合未来开展深入研究时再评估。ppt-master-main 用于演示文稿，本次无需复制。

## 来源记录

两份原样文件来自 `C:/Users/li jiayi/.codex/skills/_shared/academic-research-agent-workspace/skills/`，复制日期 2026-11-18，无本地路径运行依赖。

- deep-research/SKILL.md SHA256：`923E9D7C673F2660F633CF709AC0A270AE0FD0A844E4C899321045B50FE9F381`
- academic-paper-reviewer/SKILL.md SHA256：`EDC454315C9AB69767B6755E716D8BF4FFEC671EDE57F971D64D17A0276E4EF2`

本机来源工作区根目录未见 LICENSE；此记录不是开源授权声明，对外再分发前需确认上游许可。

## 使用方法

技能放在仓库 `.agents/skills/`，这是官方说明的项目技能目录，参见 [Build skills](https://learn.chatgpt.com/docs/build-skills)。若当前会话没有显示新技能，可重新打开项目会话；也可直接要求读取对应 SKILL.md 执行，不依赖自动发现。

每日试运行：

```text
请读取 .agents/skills/paper-tracker-daily/SKILL.md，执行一次近 7 天的论文检索，最多收录 2 篇，更新卡片、三个索引及日志。不要提交或推送。
```

首次回溯另行指定“2025-01-01 至今的重要论文”，不要把回溯与每日增量覆盖混淆。

每周综述：

```text
请读取 .agents/skills/paper-tracker-weekly/SKILL.md，为最近一个完整自然周生成周报，按实际卡片数量分析，不补凑论文。
```

## 验证与下一步

已核对两份复制文件与来源一致、技能结构及引用路径，并运行文献库基础检查。当前文献库为空，尚未验证真实检索、全文获取、去重和索引写入的完整流程；这些需要一次实际研究试运行。

建议继续采用现有项目保存长期文献，每日最多 1–2 篇，另做每周综合分析；每日推荐保存在日期目录，不创建每日分支。技能是工作说明，复制完成不代表已有定时调度。下一步先完成一次检索试运行，再选择定时执行方式和同步策略。

后续进展（2026-11-18）：已完成一次近 7 天试运行，核查 6 篇候选并收录 2 篇，卡片与索引检查通过，详见 [试跑记录](../logs/2026-11-18-trial.md)。前段“文献库为空”描述的是技能安装时状态；本次仍未验证自动调度和重复执行幂等性。

## 论文笔记模板补充

根据用户提供的 `3-research-paper-note-template-CN.md` 与 `5-survey-paper-note-template-CN.md`，在原有 14 个主章节中增加 2.1“摘要中文翻译”和 2.2“数据集—问题—解决方案”。摘要注明来源版本及翻译范围；实验表关联具体数据、问题、方法机制、验证依据和边界。综述使用领域、Taxonomy、代表性数据集及证据缺口，不硬套实验方法。

两份参考模板位于用户提供的 Water-Plant-AI-Assistant 目录，本次仅阅读，未改动源文件；其水厂项目举例不自动变成本项目的研究范围。这里沿用其数据 / 方法 / 证据对应和实验类、综述类区分的思路，未整体搬入所有栏目。两篇已有卡片已补充上述模块，本次摘要采用要点译述。
