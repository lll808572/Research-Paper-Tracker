# Codex Cloud 与自动化说明

## Codex Cloud

Codex Cloud 任务运行于云端独立工作区。
可在电脑休眠时继续运行。

创建环境：
1. 在 ChatGPT / Codex 中选择 Work in -> Cloud。
2. 连接 GitHub。
3. 选择 Research-Paper-Tracker 仓库。
4. 配置网络和所需工具。
5. 检查环境设置并发布。
6. 后续任务复用该环境。

每个新任务有自己的工作区。
重要修改必须提交到 GitHub，不能依赖临时工作区状态。

## 定时任务的重要区别

Codex Cloud 环境不是循环调度器。
不要假设发布环境后会自动每日执行。

当前需要区分：
- Codex Cloud：执行云端任务。
- ChatGPT Scheduled Tasks：安排定时任务，但网页任务不能直接访问本地文件夹。
- GitHub Actions：可以定时运行仓库中的程序。

## 推荐长期无人值守方案

GitHub Actions 定时触发 Python 检索程序。
程序调用学术检索 API 和独立配置的 AI API。
生成 Markdown 后提交到 GitHub。

注意：
ChatGPT Plus 订阅不包含通用 OpenAI API 额度。
API 调用需要独立配置和计费。

在部署前先人工运行并验证检索、总结、去重和 Git 写入。
