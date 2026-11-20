# 怎样修改论文检索要求

## 最常修改的三个文件

| 想改什么 | 编辑哪个文件 | 编辑位置 |
|---|---|---|
| 周三精确检索的主题、关键词、纳入与排除条件 | [focused_research_topics.md](../config/focused_research_topics.md) | 第 2 节刘方向、第 3 节戴方向、第 4 节筛选条件 |
| 周一、周五的原有广泛研究方向 | [research_topics.md](../config/research_topics.md) | 各方向关键词和重点关注部分 |
| 哪天检索哪个范围、每次几篇、补检和上传规则 | [automation_config.md](../config/automation_config.md) | 每周检索分工、每次周期任务、GitHub 同步部分 |

例如，希望周三更偏重工具失败，把 focused_research_topics.md 第 2 节加入：

```text
优先关注工具超时、空返回、对象错误与真实阴性观测的区别，要求论文讨论它们如何影响证据判断或 RCA 决策。
关键词增加：tool failure、missing evidence、negative evidence、observation availability。
```

这只是修改示例，没有自动加入当前范围。不要只追加一句“多关注某方向”而保留冲突排除项；应同时检查纳入标准和排除条件。

## 其他配置入口

- [search_sources.md](../config/search_sources.md)：渠道和会议 / 期刊列表。
- [paper_criteria.md](../config/paper_criteria.md)：质量、时间、优先级和数量控制。
- [paper_template.md](../templates/paper_template.md)：每篇 Markdown 的栏目，包括摘要中文翻译范围和数据集—问题—解决方案。
- [AGENTS.md](../AGENTS.md)：项目通用规则，文件保留、真实性和去重等；日常改关键词不必动它。
- `.agents/skills/paper-tracker-daily/SKILL.md`：执行流程；日常改研究范围不必修改该技能。

## 在 VS Code 中修改后怎么生效

1. 编辑并保存相应文件，检查是否有互相矛盾的规则。
2. 在源代码管理中审查、暂存并提交这些改动，再推送 GitHub。
3. 定时任务每次都读取项目里的当前配置，因此下次将使用新范围；未提交的修改会触发工作区保护并阻止运行。

当前为本地任务，本地保存的文件会被读取；提交 / 推送能保持工作区干净和多电脑一致。若以后迁移云端，必须确保配置已推送并被云端拉取。

修改 automation_config.md 中哪天用哪个范围会改变任务读取后的分工，但**修改实际运行时刻 / 触发星期，还需要在自动任务界面更新调度**。仅改文件不会修改定时器。不要手工编辑个人目录中的 automation.toml 来代替任务管理工具。

## 分类副本怎么维护

专题在 [focused_papers/rca_agent_reliability](../focused_papers/rca_agent_reliability/README.md)，按刘春泰、戴雅楠分别存完整卡片；同一论文可出现在两边。

正本在 papers/YYYY/MM/，总索引一篇一行。更新正本后，在项目终端运行：

```powershell
python scripts/sync_focused_library.py
python scripts/sync_focused_library.py --check
```

脚本若报告副本被手动修改，会停止，不覆盖；先保留并人工合并笔记。新增归类需维护 catalog.json 和分类 README。个人想法建议另存 notes.md，以免和生成内容混在一起。

本次为用户授权的批量回溯，15 篇新增笔记以摘要 / 公开页面为主、未完成逐段全文精读。后续周期每次仍最多 2 篇，专题双目录副本不翻倍计数。
