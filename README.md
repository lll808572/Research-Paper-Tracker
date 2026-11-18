# Research Paper Tracker

个人科研文献情报与知识管理系统。

## 研究方向

1. Agent / LLM
2. Time Series Analysis
3. Root Cause Analysis (RCA)
4. Anomaly Detection
5. Cross-domain Research

## 项目目标

持续追踪 2025 年以来的高质量研究论文，
完成检索、筛选、去重、阅读、总结和研究趋势分析。

## 核心工作流

论文检索
-> 相关性筛选
-> 论文去重
-> 全文阅读
-> Markdown 总结
-> 更新索引
-> 每周研究综述

## 目录说明

- config/: 检索和筛选配置
- templates/: 论文及周报模板
- papers/: 单篇论文总结
- digests/: 每周研究综述
- indexes/: 文献总索引
- logs/: 自动化运行日志
- scripts/: 项目维护脚本
- docs/: 使用和部署说明

## 基本原则

- 不编造论文、作者、DOI、实验数据和引用。
- 区分预印本、投稿论文和正式录用论文。
- 每篇论文必须有原始来源链接。
- 严格去重，不重复创建论文卡片。
- 无高质量论文时允许当日零收录。
- 摘要分析不能冒充全文精读。
- API Key 和密码不得进入 Git。
- 不将大型 PDF 批量提交到 Git。
- 不为每日论文创建 Git 分支。

## 推荐使用方式

GitHub Private Repository 保存长期知识库。
Codex 用于研究分析和项目维护。
Zotero 用于原始文献及 PDF 管理。

详见 docs/ 目录。

## 项目研究技能

已配置每日论文整理、每周研究综述，以及文献比较和批判阅读辅助技能。
使用方法、来源与当前验证范围见 [研究技能说明](docs/SKILLS_GUIDE.md)。
技能文件位于 `.agents/skills/`；定时调度需另行配置。
