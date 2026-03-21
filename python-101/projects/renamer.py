# Move and rename all .png files on your Desktop
from pathlib import Path

down = Path.home() / "Downloads" / "Kurs"
sorted_path = Path.home() / "Pictures" / "zweite_auslese"
# Identify all screenshots on your Desktop

# Create a new directory
sorted_path.mkdir(parents=True, exist_ok=True)
# Move and rename all screenshots
for i, filepath in enumerate(down.iterdir(), start=1):
    if filepath.is_file() and filepath.suffix.lower() == ".jpg":
        new_name = f"sorted_pic_{i}.jpg"

        new_filepath = sorted_path / new_name

        filepath.replace(new_filepath)
