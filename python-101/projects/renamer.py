# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

from pathlib import Path

desktop = Path("/home/jayram/Desktop")
pictures = Path("/home/jayram/Desktop/Pictures2")

pictures.mkdir(exist_ok=True)

for filepath in desktop.rglob("*"):
    if filepath.suffix == ".jpg":
        new_filepath = filepath.joinpath(filepath.name)
        filepath.replace(new_filepath)