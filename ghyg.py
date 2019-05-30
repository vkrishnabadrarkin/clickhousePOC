import csv
csv_file = "info.csv"
csv_columns = ['name','dept','year','cpi']
data = {}

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                # if flagg ==0:
                #writer.writeheader()
                # flagg = 1
        for rowdata in data:
            writer.writerow(rowdata)
except IOError:
     print("I/O error")