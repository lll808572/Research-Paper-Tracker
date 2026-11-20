# Automation Configuration

## 目标频率

周期检索：每周一、三、五 08:30 Asia/Shanghai，间隔 2、2、3 天。
每次最多收录 2 篇，允许 0 篇；不再每天执行。
每周综述：保留按需生成，本次不创建独立周报定时任务。

## 每周检索分工（2026-11-20 用户确认）

| 北京时间 | scope | 读取的范围文件 | 内容 |
|---|---|---|---|
| 周一 08:30 | general | config/research_topics.md | 原有 Agent、时间序列、RCA、异常检测及交叉研究 |
| 周三 08:30 | focused | config/focused_research_topics.md | 两份开题报告的证据审计 / 纠错与证据充分性 / 停止支线 |
| 周五 08:30 | general | config/research_topics.md | 原有广泛范围 |

每次仍最多 2 篇，总量按独立论文计数，不因双目录副本翻倍。
任务必须读取上表及对应范围文件，不从旧聊天或自动任务提示恢复过期关键词。
更改星期分工可编辑本表；更改触发时间或星期还需要通过 Codex 自动任务界面 / 工具更新调度，单改文件不会改变实际触发时刻。

## 每次周期任务

- 检查新增论文及重要版本更新。
- 检索 2025 年以来相关研究。
- general 与 focused 各自维护成功覆盖时间，不能用周五广泛检索的截止推进周三专题覆盖。覆盖所选 scope 上次成功 covered_to 至本次开始；可重叠 24 小时处理延迟，严格去重。该 scope 无成功周期记录时默认近 7 天；旧有未标 scope 的周期 / daily 记录视为 general。
- 首次历史回溯应单独执行。
- 每次最多收录 2 篇，不为补足数量降低质量。
- 严格去重。
- 更新索引与运行日志。

## 当前执行方案与 GitHub 同步

使用 Codex 本地定时任务，关联本项目聊天；电脑需开机、联网并保持应用运行。
任务名称：论文追踪与 GitHub 同步（每周三次）；任务 ID：`github`，已创建为 ACTIVE。
运行条件参考：[官方定时任务说明](https://learn.chatgpt.com/docs/automations)。
仓库：`https://github.com/lll808572/Research-Paper-Tracker`；分支：`main`。

用户已授权周期检索后自动提交和推送本次预期文件：

1. 检查仓库、分支、远程地址及工作区状态。存在用户未提交修改、已暂存文件或未解释的本地领先提交时停止，保留现场并报告；不自动 stash、reset 或覆盖。
2. 工作区干净时执行 `git pull --ff-only origin main`；失败或分叉即停止。
3. 按 `.agents/skills/paper-tracker-daily/SKILL.md` 和项目模板执行增量研究；技能名称沿用 daily，但调度频率以本配置为准。必须包含摘要翻译范围、数据集—问题—解决方案模块。
   对 focused 运行，先读 config/focused_research_topics.md，按两条支线筛选和分类。正本仍在 papers/YYYY/MM/，专题副本置于 focused_papers/rca_agent_reliability/ 下；维护 catalog.json 及分类 README，运行同步和只读校验。副本不重复写入 papers.csv。general 收录若明确符合专题，也可按同一规则归类。
4. 检查卡片、三个索引、日志、标识去重和链接；运行基础验证脚本并检查差异。
5. 仅显式暂存本次实际修改的 `papers/`、三个索引、`logs/`，以及本次生成的 `focused_papers/rca_agent_reliability/` 副本、catalog.json 与分类 README。不使用 `git add .`，不把设置、附件或用户笔记混入。新增路径必须逐个审查，不能把整个专题目录中用户的 notes 文件顺便提交。
6. 提交前检查暂存差异及文件清单，再提交并 `git push origin main`。不创建每日分支，不强制推送。远程并发更新导致推送拒绝时，保留本地提交并报告，不自动改写历史或反复重试。
7. 检索状态与同步状态分开记录：推送前日志标注同步 pending；回复中以实际推送结果说明 synced 或 failed，不能将本地整理成功称为已上传。失败检索日志可提交，但不得推进研究成功覆盖时间。

本方案尚需首个计划运行验证调度、研究与自动上传的端到端执行。此前手工试跑不作为定时执行成功证据。

## 每周任务

- 汇总本周新增论文。
- 生成研究方向分布。
- 对比技术路线。
- 分析跨方向联系。
- 推荐 2-3 篇精读论文。
- 提出可验证的研究问题。

## 恢复与补偿

每次运行前读取上次成功时间。

若存在漏检区间：
- 补充检索遗漏时间段。
- 检查重复论文。
- 不重复创建卡片。
- 保留每次任务状态。

记录：
- last_attempt_at
- last_success_at
- covered_from
- covered_to
- status
- scope（general / focused；用户批量回溯用 focused-backfill，不推进任何周期覆盖时间）

## 重要架构说明

Codex Cloud 可以运行云端任务，但每个任务拥有独立工作区。
云端任务可以在个人电脑休眠时继续运行。

Codex Cloud 环境本身不等于周期调度器。
不能假设创建 Cloud Environment 后就自动每日运行。

当前可选的周期调度方式：
1. GitHub Actions + 可调用的模型 API。
2. 支持云端项目访问的 ChatGPT 定时任务。
3. 本地 Codex Scheduled Task。

若采用 GitHub Actions，需要单独配置 AI API 凭据。
ChatGPT 订阅不等于 API 额度。

自动化部署前必须验证：
- 检索 API 可访问。
- AI API 可用。
- GitHub 写入权限正确。
- 重复检测正常。
- 失败不会误更新成功时间。
