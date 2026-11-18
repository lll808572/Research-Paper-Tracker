from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
INDEX = ROOT / "indexes" / "papers.csv"

errors = []
markdown_files = list(PAPERS.rglob("*.md"))

print(f"论文 Markdown 文件数量：{len(markdown_files)}")

for path in markdown_files:
    content = path.read_text(encoding="utf-8-sig")

    if not content.strip():
        errors.append(f"空文件：{path.relative_to(ROOT)}")

    if content.count("---") < 2:
        errors.append(f"缺少基本元数据区：{path.relative_to(ROOT)}")

if INDEX.exists():
    with INDEX.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
        print(f"CSV 行数（含表头）：{len(rows)}")
else:
    errors.append("缺少 indexes/papers.csv")

if errors:
    print("\n检查发现问题：")
    for item in errors:
        print("-", item)
    raise SystemExit(1)

print("文献库基础检查通过。")
