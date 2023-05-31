# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

from pathlib import Path
import os

desktop = Path("/home/jayram/Desktop")
destination_dir = Path("/home/jayram/Desktop/Pictures2")
destination_dir.mkdir(exist_ok=True)

files = desktop.glob("*")

counter = 1

for file in files:
    if file.suffix == ".jpg":
        new_filename = f"NewFileName_{counter}{file.suffix}"
        destination_path = destination_dir/new_filename
        os.rename(file, destination_path)
        print(f"Moved and renamed {file.name} to {new_filename}")
        counter +=1