from pathlib import Path
import re

solutions_dir = Path("solutions")
readme = Path("README.md")

rows = []

for file in sorted(solutions_dir.glob("*.py")):
    content = file.read_text()

    problem = re.search(r"# Problem:\s*(.+)", content)
    difficulty = re.search(r"# Difficulty:\s*(.+)", content)
    language = re.search(r"# Language:\s*(.+)", content)

    if not problem:
        continue

    number = file.stem.split("_")[0]

    rows.append(
        f"| {number} | {problem.group(1)} | "
        f"{difficulty.group(1) if difficulty else '-'} | "
        f"{language.group(1) if language else 'Python'} |"
    )

table = """| Sl.No. | Problem | Difficulty | Language |
|---|---------|------------|----------|
""" + "\n".join(rows)

text = readme.read_text()

start = "<!-- START_PROBLEMS -->"
end = "<!-- END_PROBLEMS -->"

new_text = re.sub(
    rf"{re.escape(start)}.*?{re.escape(end)}",
    f"{start}\n{table}\n{end}",
    text,
    flags=re.DOTALL
)

readme.write_text(new_text)