import os
import csv
#Directions..
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
election_data = os.path.join('election_data')
#the file online downloaded as a tab, so idk if it will come out right

#define my variables
total_votes= 0
candidates=["Khan", "Correy", "Li", "O'Tooley"]
candidates_v=["Khan_v", "Correy_v", "Li_v", "tooley_v"]
Khan_v=0
Correy_v=0
Li= 0
tooley_v=0

#open the file
with open(election_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#loop through data to get the if then statement for each candidate votes
    for row in csvfile:
        total_votes +=1
        
        if row[2] == "Khan": 
            Khan_v +=1
        elif row[2] == "Correy":
            Correy_v +=1
        elif row[2] == "Li": 
            Li_v +=1
        else row[2] == "O'Tooley":
            tooley_v +=1
# get percentage of votes
Khan_percent=((Khan_v/total_votes) *100)
Correy_percent=((Correy_v/total_votes)*100)
Li_percent=((Li_v/total_votes)*100)
tooley_percent=((tooley_v/total_votes)*100)
#get the winner
winner=(max(candidates_v))
 print("Election Results")
    print(f"Total Votes: {total_votes}")
    print(f"Khan %{(Khan_percent)} ({Khan_v)})")
    print(f"Correy %{str(Correy_percent)} ({(Correy_v)})")
    print(f"Li %{str(Li_percent)} ({(Li_v)})")
    print(f"O'Tooley %{(tooley_percent)} ({(tooley_v)})")
    print(f"Winner: {(winner)}")