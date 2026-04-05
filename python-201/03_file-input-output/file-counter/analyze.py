# Use the `csv` module to read in and count the different file types.

import csv

with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictWriter(csvfile, fieldnames=["ISO", "ZIP", "MKV", "PNG", "JSON"])
    counts = list(reader)
