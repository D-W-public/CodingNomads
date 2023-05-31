# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

from pathlib import Path


source_dir = Path("/home/jayram/Documents/CodingNomads")

py_lst = []

for file in source_dir.rglob("*"):
    if file.suffix == ".py":
        py_lst.append(file)

print(*py_lst, sep="\n")

