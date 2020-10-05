import os
import csv

path = os.path.join("PyPoll","Resources","election_data.csv")

Khan = []
Tooley = []
Li = []
Correy = []

with open(path) as election_file:

    reader = csv.reader(election_file)
    header = next(reader)
    count = sum(1 for votes in reader)

print("Total Votes: " + str(count))

with open(path) as election_file:

    reader = csv.reader(election_file, delimiter=",")
    header = next(reader)

    for votes in reader:

        if votes[2] == "O'Tooley":
            Tooley.append(votes)
        elif votes[2] == "Li":
            Li.append(votes)
        elif votes[2] == "Khan":
            Khan.append(votes)
        else:
            Correy.append(votes)

tooley_count = sum(1 for tvote in Tooley)
tooley_percent = tooley_count / count * 100
print("O'Tooley: " + str(round(tooley_percent, 2)) + "%" + " " + "(" + str(tooley_count) + ")") 

li_count = sum(1 for lvote in Li)
li_percent = li_count / count * 100
print("Li: " + str(round(li_percent, 2)) + "%" + " " + "(" + str(li_count) + ")")

khan_count = sum(1 for kvote in Khan)
khan_percent = khan_count / count * 100
print("Khan: " + str(round(khan_percent, 2)) + "%" + " " + "(" + str(khan_count) + ")")

correy_count = sum(1 for cvote in Correy)
correy_percent = correy_count / count * 100
print("Correy: " + str(round(correy_percent, 2)) + "%" + " " + "(" + str(correy_count) + ")")

winner_list = [tooley_count, li_count, khan_count, correy_count]
candidate_list = ["O'Tooley", "Li", "Khan", "Correy"]

winner_index = winner_list.index(max(winner_list))
winner = candidate_list[winner_index]
print("Winner: " + winner)
