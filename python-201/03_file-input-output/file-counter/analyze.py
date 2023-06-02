# Use the `csv` module to read in and count the different file types.
import csv
from pathlib import Path

destination = Path("/home/jayram/Documents/CodingNomads/python-201/03_file-input-output/file-counter/filecounts.csv")

with open(destination, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)