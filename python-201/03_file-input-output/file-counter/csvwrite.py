# Write the file counts to a `.csv` file.
import csv
from pathlib import Path

test = Path.home() / "Documents" / "test"
output = (
    Path.home()
    / "CodingNomads"
    / "python-201"
    / "03_file-input-output"
    / "file-counter"
    / "filecounts.csv"
)
filetypes = {}

for item in test.iterdir():
    if item.is_file():
        ext = item.suffix

        if ext in filetypes:
            filetypes[ext] += 1

        else:
            filetypes[ext] = 1

with output.open("a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [
        filetypes[".iso"],
        filetypes[".zip"],
        filetypes[".mkv"],
        filetypes[".png"],
        filetypes[".json"],
    ]
    countwriter.writerow(data)
