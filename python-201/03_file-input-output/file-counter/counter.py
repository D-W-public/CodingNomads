#import nessecary modules
from pathlib import Path
import os
import csv


#set up Path and dict 

source = Path("/home/jayram/Desktop")
destination = Path("/home/jayram/Documents/CodingNomads/python-201/03_file-input-output/file-counter/filecounts.csv")

file_counts = {}
#count the files andfeed count into dict

for root, dirs,files in os.walk(source):
    for file in files:
        file_ext = os.path.splitext(file)[1]
        if file_ext in file_counts:
            file_counts[file_ext] += 1
        else:
            file_counts[file_ext] = 1

print(file_counts)

# save values to csv file


with open(destination, "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(file_counts.values())
   
    
