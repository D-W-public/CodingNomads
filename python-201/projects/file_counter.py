# Add the code for the file counter script that you wrote in the course.

from pathlib import Path

down = Path.home() / "Downloads"

filetypes = {}

for item in down.iterdir():
    if item.is_file():
        ext = item.suffix

        if ext in filetypes:
            filetypes[ext] += 1

        else:
            filetypes[ext] = 1

print(filetypes)
