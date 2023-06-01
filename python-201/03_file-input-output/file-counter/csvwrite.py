# Write the file counts to a `.csv` file.
with open(destination, "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(file_counts.values())