#import os module & csv module for reading csv files
import os
import csv

PyBank_csv = os.path.join('budget_data.csv')

print(PyBank_csv)
with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csvreader)
