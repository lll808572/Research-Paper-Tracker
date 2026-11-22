from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
INDEX = ROOT / "indexes" / "papers.csv"

errors = []
with INDEX.open("r", encoding="utf-8-sig", newline="") as f:
    records = list(csv.DictReader(f))
markdown_files = [ROOT / row['local_file'] for row in records]
if len({r['paper_id'] for r in records}) != len(records):
    errors.append('CSV 存在重复论文标识')
if len(set(markdown_files)) != len(markdown_files):
    errors.append('CSV 存在重复主卡片路径')

print(f"论文 Markdown 文件数量：{len(markdown_files)}")

for path in markdown_files:
    if not path.resolve().is_relative_to(ROOT) or not path.is_file():
        errors.append(f'缺失或非法卡片路径：{path}')
        continue
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
