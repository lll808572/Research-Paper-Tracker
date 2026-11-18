# Automation Configuration

## 目标频率

每日检索：建议 08:30 Asia/Shanghai。
每周综述：建议周日 20:00 Asia/Shanghai。

## 每日任务

- 检查新增论文及重要版本更新。
- 检索 2025 年以来相关研究。
- 优先分析最近 24 小时新增记录。
- 首次历史回溯应单独执行。
- 每日最多收录 1-2 篇。
- 严格去重。
- 更新索引与运行日志。

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
