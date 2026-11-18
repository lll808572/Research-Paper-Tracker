param(
    [switch]$Push
)

$ErrorActionPreference = "Stop"

$Root = Split-Path $PSScriptRoot -Parent
Set-Location $Root

if (-not (Test-Path ".git")) {
    Write-Error "当前目录尚未初始化 Git。"
}

Write-Host "检查工作区..." -ForegroundColor Cyan
git status --short

if ($LASTEXITCODE -ne 0) { throw "Git 状态检查失败" }

Write-Host "拉取远程更新..." -ForegroundColor Cyan
git pull --ff-only

if ($LASTEXITCODE -ne 0) {
    throw "拉取失败。请先处理本地修改或分支冲突。"
}

if ($Push) {
    Write-Host "Push 不会自动提交本地修改。" -ForegroundColor Yellow
    Write-Host "请先审查 git diff，再手动 commit 和 push。"
}

Write-Host "同步完成。" -ForegroundColor Green
