import csv
import os.path

class CsvFunctions:

    def writer(self,header,data,filename):
        with open (filename, "w", newline = "") as csvfile:
            rows = csv.writer(csvfile)
            rows.writerow(header)
                
            for item in data:
                rows.writerow(item)
                