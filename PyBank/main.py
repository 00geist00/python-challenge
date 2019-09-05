#import os module & csv module for reading csv files
import os
import csv

#create trackers
totalMonths = 0
totalRev = 0
pastRev = 0
highestIncRev = 0
lowestDecRev = 99999999999
#create lists to store revenue change
revChange = []

PyBank_csv = "/Users/kaseygeist/Desktop/python-challenge/PyBank/budget_data.csv"

with open(PyBank_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   #print(csvreader)

   for row in csvreader:
        #count total months (aka rows)
        totalMonths = totalMonths + 1
        #count total revenue by adding up each value in the 2nd column
        totalRev = totalRev + (int(row[1]))
        #create a variable that will count the revenue changes
        monthlyRevChange = int(row[1]) - pastRev
        pastRev = int(row[1])
        #create a new list that to keep track of all the monthly changes in rev (for max and min)
        revChange.append(monthlyRevChange)
        #calculate the average change in revenue
        avgRevChange = round(sum(revChange)/totalMonths)

        #loop through to find the greatest increase in revenue in the "monthlyRevChange" column and store as "highestIncRev" with "highestIncMonth" from the first column (date)
        if (monthlyRevChange > highestIncRev):
            highestIncMonth = row[0]
            highestIncRev = monthlyRevChange 
        #loop through to find the greatest decrease in revenue in the "monthlyRevChange" column and store as "lowestIncRev" with "lowestIncMonth" from the first column (date)
        if (monthlyRevChange < lowestDecRev):
            lowestDecMonth = row[0]
            lowestDecRev = monthlyRevChange

#create varible to hold finanical analysis results and use f-strings for formatting
Results = (
f"Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {totalMonths} \n"
f"Total Revenue: ${totalRev} \n"
f"Average Revenue Change: ${avgRevChange} \n"
f"Greatest Increase in Revenue: {highestIncMonth} (${highestIncRev}) \n"
f"Greatest Decrease in Revenue: {lowestDecMonth} (${lowestDecRev}) \n")
print(Results)

#write a text file in order to export results to text file
outputtxt = "/Users/kaseygeist/Desktop/python-challenge/PyBank/budget_data_output.txt"
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Results)