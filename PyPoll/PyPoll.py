import os
import csv

#Open and read csv
#print(os.getcwd())
csvpath = os.path.join('Resources', 'election_data.csv')

#Create lists for candadites and define variables
votes = 0
candidateDic={}

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
  
#Find Candidates and Add to Dic as Keys 
    for row in csvreader:

        votes = votes+1

        if row[2] not in candidateDic:
           candidateDic[row[2]] = 0

#Sum Total Number of Votes Cast
        candidateDic[row[2]] = candidateDic[row[2]]+1

#Count Total Votes of Each Candidate
khanVotes = candidateDic["Khan"]
correyVotes = candidateDic["Correy"]
liVotes = candidateDic["Li"]
otooleyVotes = candidateDic["O'Tooley"]

#Calculate Percentage of Votes for Each Candidate
khanPercentage = round((candidateDic["Khan"] / votes) * 100, 2)
correyPercentage = round((candidateDic["Correy"] / votes) * 100, 2)
liPercentage = round((candidateDic["Li"] / votes) * 100, 2)
otooleyPercentage = round((candidateDic["O'Tooley"] / votes) * 100, 2)

#Calculate Winner based on Popular Vote
winner=''
final = 0
for candidate in candidateDic:
    
    v = candidateDic[candidate]/votes

    if v>final:
        final=v
        winner=candidate

#Print Data in Terminal
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {votes} ")
print("-----------------------------")
print(f"Khan: {khanPercentage}00% ({khanVotes})")
print(f"Correy: {correyPercentage}00% ({correyVotes})")
print(f"Li: {liPercentage}00% ({liVotes})")
print(f"O'Tooley: {otooleyPercentage}00% ({otooleyVotes})")
print("------------------------------")
print(f"Winner: {winner} ")
print("------------------------------")

#Write and Export File

output_file = os.path.join("PyPoll_Analysis.csv")

with open(output_file, "w", newline="") as xfile:

    column_title_row = "Data Type, Value" + '\n'
    xfile.write(column_title_row) 
    xfile.write("Total Votes:, " + str(votes) + '\n')
    xfile.write("Khan:, " + str(khanPercentage) + "00% (" + str(khanVotes) + ")" + '\n')
    xfile.write("Correy:, " + str(correyPercentage) + "00% (" + str(correyVotes) + ")" + '\n')
    xfile.write("Li:, " + str(liPercentage) + "00% (" + str(liVotes) + ")" + '\n')
    xfile.write("O'Tooley:, " + str(otooleyPercentage) + "00% (" + str(otooleyVotes) + ")" + '\n')
    xfile.write("Winner:, " + winner + '\n')

    xfile.close()