from pathlib import Path
list_py = Path(__file__).parent.rglob("*.py")
current_file = Path(__file__).resolve()
count = 0
for each in list_py:
    if each.resolve() == current_file:
        continue
    with open(each,"r",encoding='utf-8') as f:
        for lines in f:
            if lines.strip():
                count += 1
print(count)