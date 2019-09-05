#import os module & csv module for reading csv files
import os
import csv

#create trackers
totalVotes = 0
candidate = ""
candidateVotes = {}
candidatePercentages = {}
winnerVotes = 0
winner = ""

PyPoll_csv = "/Users/kaseygeist/Desktop/python-challenge/PyPoll/election_data.csv"

with open(PyPoll_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   #print(csvreader)

   for row in csvreader:
        #count total votes (aka rows)
        totalVotes = totalVotes + 1
        #assign candidate to the 3rd column in the data
        candidate = row[2]
        #tally votes by candidate candidates
        if candidate in candidateVotes:
            candidateVotes[candidate] = candidateVotes[candidate] + 1
        else:
            candidateVotes[candidate] = 1

    #calculate vote percentage for each candidate and identify winner
for person, vote_count in candidateVotes.items():
    candidatePercentages[person] = '{0:.0%}'.format(vote_count / totalVotes)
    if vote_count > winnerVotes:
        winnerVotes = vote_count
        winner = person

#print results
print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for person, vote_count in candidateVotes.items():
    print(f"{person}: {candidatePercentages[person]} ({vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#write a text file in order to export results to text file
outputtxt = "/Users/kaseygeist/Desktop/python-challenge/PyPoll/poll_data_output.txt"

filewriter = open(outputtxt, mode = 'w')

filewriter.write(f"Election Results\n")
filewriter.write("-------------------------\n")
filewriter.write(f"Total Votes: {totalVotes}\n")
filewriter.write("-------------------------\n")
for person, vote_count in candidateVotes.items():
    filewriter.write(f"{person}: {candidatePercentages[person]} ({vote_count})\n")
filewriter.write("-------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("-------------------------\n")