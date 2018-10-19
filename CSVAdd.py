import os, csv

with open("k.csv", 'w') as f:
    writer = csv.writer(f)
    for path, dirs, files in os.walk("E:\Movies\English"):
        for filename in files:
            writer.writerow([filename])
