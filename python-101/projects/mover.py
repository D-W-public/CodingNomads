# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
from pathlib import Path
# Find the path to my Desktop
target = Path("/home/jayram/Desktop/Pictures")
source = Path("/home/jayram/Desktop")
# Create a new folder
target.mkdir(exist_ok=True)

# Filter for screenshots only
for filepath in source.rglob("*"):
    if filepath.suffix == ".jpg":
        new_filepath = target.joinpath(filepath.name)
        filepath.replace(new_filepath)

# Create a new path for each file

# Move the screenshot there