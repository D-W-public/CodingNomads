from pathlib import Path
import os
#set up the path to the directory

source = Path("/home/jayram/Desktop")

file_counts = {}
#count the files
#feed count into dict

for files in os.walk(source):
    for file in files:
        file_ext = os.path.splitext(file)[1]
        if file_ext in file_counts:
            file_counts[file_ext] += 1
        else:
            file_counts[file_ext] = 1

print(file_counts)
#with open("filecounts2.csv", "a") as csvfile