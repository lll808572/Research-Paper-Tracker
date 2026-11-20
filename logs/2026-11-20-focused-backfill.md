# 专题批量整理与调度更新

- 日期：2026-11-20，Asia/Shanghai；记录时间窗 15:52:59 至 16:01:56。
- 类型 / scope：focused-backfill，用户明确要求整批整理上轮确认论文，并允许两位学长目录保存重复副本。
- 检索回溯范围：2025-01-01 至 2026-11-20；不是本次周期窗口新增 15 篇。
- 来源：复核上轮候选的 arXiv / ACL Anthology / PMLR 原始元数据，结合此前部分正文及作者公开版；没有上传两份 DOCX 内容到外部模型。
- 本轮打开 15 篇主源页面；此前补充核查的 Stalled 一并整理。新增查询字符串 0（通过已核实原始标识复查）；检索总命中数不适用。
- 新增正本卡片 15；复用已有 CLEW 1；专题独立论文 16，刘春泰分类 12 份、戴雅楠分类 11 份，共 23 份完整副本。
- 既有库 4 篇，新增后总库 19 篇、CSV 19 行记录；同一 DOI / arXiv ID 不重复入库。15 个新候选与原库重复移除 0；CLEW 为已知复用，新增独立记录 0；分类之间重复不计入论文数量。
- 论文来源与版本可查各卡片第 14 节和专题 catalog；本次未下载大型 PDF，也未执行论文代码。
- 分析级别：摘要 / 官方公开页面为主的初步阅读笔记，包含摘要要点译述和数据集—问题—解决方案；15 篇均 full_text_reviewed=false，不冒充完整精读或独立复现。
- 运行状态 partial：文件整理和调度修改完成；Flow-of-Action / Stalled 的出版页独立核验及若干录用声明仍未完成，保留作者来源与未核实标记。本次没有把这些声明直接标为官方录用。
- 失败 / 限制：继承此前 Flow-of-Action ACM 页面 403 的核验缺口；未补造未知日期、实验设置、公式、代码开放状态或精确分数。
- 周期 last_success_at / covered_to 均不推进；这是一次性回溯，不应让后续周三漏检近期工作。

## 已落地的目录和配置

- focused_papers/rca_agent_reliability/README.md 为专题总入口；liu_chuntai 与 dai_yanan 各自有阅读索引和完整卡片。
- 正本在 papers/YYYY/MM/，总 CSV 一篇一行。catalog.json 维护分类与同步哈希；sync_focused_library.py 同步且保护手改副本，兼容 Git 的 LF / CRLF 转换。
- config/focused_research_topics.md 为可编辑的精确范围：刘方向、戴方向、关键词、纳入 / 排除规则、分类要求。
- config/automation_config.md 明确周一 / 周五 general，周三 focused，并要求两种 scope 分别维护覆盖时间。
- AGENTS.md、daily 技能和 README 追加专题入口；docs/EDIT_SEARCH_REQUIREMENTS.md 解释修改入口、保存提交和实际调度的区别。
- 自动任务 github 通过工具更新并保持 ACTIVE，原每周一 / 三 / 五北京时间 08:30 不变；任务每次读配置，避免关键词在提示和文件间漂移。仍为本地执行环境，没有声称已迁移云端。
- 已有 CLEW 仅将 RT-FM 的相关卡片链接改为仓库 URL，使完整复制后链接仍有效，未改写原分析内容。

## 检查

- 原 validate_library.py 通过：19 个正本、CSV 含表头 20 行。
- 标识唯一性、CSV 与正本对应、14 个主章节、两个新增模块、专题目录本地链接均通过。
- sync_focused_library.py --check 通过：16 篇、23 副本。
- 临时目录功能检查通过：正本更新会同步，单纯 CRLF 差异不误报；副本手改会拒绝覆盖且不写入部分 catalog。
- git diff --check 通过；所有新增文件将逐路径暂存，忽略 .cache 中临时构建材料。
- Git 同步 pending（提交前记录），以本次提交及实际推送结果为准。
