#Import modules
import os
import csv

#Declare Path
path = os.path.join("PyPoll","Resources","election_data.csv")

#Define needed lists
Khan = []
Tooley = []
Li = []
Correy = []

#Read File
with open(path) as election_file:
    reader = csv.reader(election_file)

    #Skip Header
    header = next(reader)

    #Count number of rows for total votes
    count = sum(1 for votes in reader)

#Read File...again
with open(path) as election_file:
    reader = csv.reader(election_file, delimiter=",")

    #Skip header...again
    header = next(reader)

    #Loop through file for individual vote count and append to seperate lists
    for votes in reader:

        if votes[2] == "O'Tooley":
            Tooley.append(votes)
        elif votes[2] == "Li":
            Li.append(votes)
        elif votes[2] == "Khan":
            Khan.append(votes)
        else:
            Correy.append(votes)

#Tally votes for each candidate and find percentage
tooley_count = sum(1 for tvote in Tooley)
tooley_percent = tooley_count / count * 100

li_count = sum(1 for lvote in Li)
li_percent = li_count / count * 100

khan_count = sum(1 for kvote in Khan)
khan_percent = khan_count / count * 100

correy_count = sum(1 for cvote in Correy)
correy_percent = correy_count / count * 100

#Create lists for candidate vote count and candidates
#Ensure indexes for both match their respective indexes
winner_list = [tooley_count, li_count, khan_count, correy_count]
candidate_list = ["O'Tooley", "Li", "Khan", "Correy"]

#Determine highest vote count
winner_index = winner_list.index(max(winner_list))
winner = candidate_list[winner_index]

#Output results in terminal
print("Election Results")
print("------------------------")
print("Total Votes: " + str(count))
print("------------------------")
print("O'Tooley: " + str(round(tooley_percent, 2)) + "%" + " " + "(" + str(tooley_count) + " votes)") 
print("Li: " + str(round(li_percent, 2)) + "%" + " " + "(" + str(li_count) + " votes)")
print("Khan: " + str(round(khan_percent, 2)) + "%" + " " + "(" + str(khan_count) + " votes)")
print("Correy: " + str(round(correy_percent, 2)) + "%" + " " + "(" + str(correy_count) + " votes)")
print("------------------------")
print("Winner: " + winner)

#Output results in seperate text file
output = os.path.join("PyPoll","Analysis","election_results.txt")

with open(output, 'w') as txt_file:
     
    txt_file.write("Election Results" + os.linesep)
    txt_file.write("------------------------" + os.linesep)
    txt_file.write("Total Votes: " + str(count) + os.linesep)
    txt_file.write("------------------------" + os.linesep)
    txt_file.write("O'Tooley: " + str(round(tooley_percent, 2)) + "%" + " " + "(" + str(tooley_count) + " votes)" + os.linesep)
    txt_file.write("Li: " + str(round(li_percent, 2)) + "%" + " " + "(" + str(li_count) + " votes)" + os.linesep)
    txt_file.write("Khan: " + str(round(khan_percent, 2)) + "%" + " " + "(" + str(khan_count) + " votes)" + os.linesep)
    txt_file.write("Correy: " + str(round(correy_percent, 2)) + "%" + " " + "(" + str(correy_count) + " votes)" + os.linesep)
    txt_file.write("------------------------" + os.linesep)
    txt_file.write("Winner: " + winner + os.linesep)
