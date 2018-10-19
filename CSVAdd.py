#Store the names of the files in a folder to a CSV file

import os, csv

with open("/**/", 'w') as f:                    #Insert the name of the CSV File that should store the names of the files in the folder
    writer = csv.writer(f)
    for path, dirs, files in os.walk("/**/"):   #Insert name of the directory within the /**/ and remove the /**/
        for filename in files:
            writer.writerow([filename])
