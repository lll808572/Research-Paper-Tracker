# GitHub 上传与协作指南

## 一、创建远程仓库

1. 登录 https://github.com/
2. 点击右上角 +。
3. 选择 New repository。
4. Repository name：Research-Paper-Tracker。
5. 选择 Private。
6. 不要勾选额外创建 README、License 或 .gitignore。
7. 点击 Create repository。

## 二、初始化本地 Git

在项目根目录执行：

git init
git branch -M main
git add .
git status
git commit -m "Initial Research Paper Tracker project"

## 三、连接 GitHub

将下面地址替换为自己的仓库地址：

git remote add origin https://github.com/USERNAME/Research-Paper-Tracker.git

git push -u origin main

## 四、其他电脑获取项目

首次：

git clone https://github.com/USERNAME/Research-Paper-Tracker.git

之后：

git pull --ff-only

## 五、提交自己的修改

先拉取：

git pull --ff-only

查看修改：

git status
git diff

提交：

git add .
git commit -m "Update paper notes"
git push

## 六、邀请协作者

仓库页面：
Settings -> Collaborators -> Add people。

输入对方 GitHub 用户名并发送邀请。
对方接受邀请后才能访问私有仓库。

注意：个人账户拥有的私有仓库中，
Collaborator 通常具有读写权限。
如果只需要给其他人只读权限，
考虑公开仓库或组织仓库。

## 七、安全要求

- 不共享 GitHub 账号密码。
- 不上传 API Key。
- 不上传个人访问令牌。
- 不上传私有 PDF。
- 不将 .env 文件提交到 Git。
