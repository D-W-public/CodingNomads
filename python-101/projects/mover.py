# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib

# Find the path to my Desktop
down = pathlib.Path.home() / "Downloads"
# Create a new folder
new_path = pathlib.Path.home() / "Pictures" / "down_sorted"
new_path.mkdir(exist_ok=True)
# Filter for screenshots only

for filepath in down.iterdir():
    if filepath.suffix == ".jpg":
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshot there
        filepath.replace(new_filepath)
