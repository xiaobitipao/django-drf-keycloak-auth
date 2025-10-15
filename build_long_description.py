from pathlib import Path

files = ["README.md", "CHANGELOG.md"]
output = Path("LONG_DESCRIPTION.md")

with output.open("w", encoding="utf-8") as out_file:
    for file in files:
        out_file.write(Path(file).read_text(encoding="utf-8"))
        out_file.write("\n\n")
