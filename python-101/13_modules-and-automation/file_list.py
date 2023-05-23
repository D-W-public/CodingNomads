from pathlib import Path

path = Path("/home/jayram/Desktop")

for filepath in path.iterdir():
    print(filepath.name)