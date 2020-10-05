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
li_count = sum(1 for lvote in Li)
khan_count = sum(1 for kvote in Khan)
correy_count = sum(1 for cvote in Correy)

print(tooley_count)
print(li_count)
print(khan_count)
print(correy_count)