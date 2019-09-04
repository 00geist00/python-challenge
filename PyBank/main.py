#import os module & csv module for reading csv files
import os
import csv


PyBank_csv = os.path.join("Resources","budget_data.csv")

with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csvreader)