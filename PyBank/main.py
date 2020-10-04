import os
import csv

path = os.path.join('Resources', 'budget_data.csv')
change = []
net = 0

with open(path) as budget_file:

    reader = csv.reader(budget_file, delimiter=",")
    header = next(reader)
    count = sum(1 for row in reader)

with open(path) as budget_file:

    reader = csv.reader(budget_file, delimiter=",")
    header = next(reader)

    profit_loss = [int(profit[1]) for profit in reader]
            
    
            

    

print("Total Months:" + " " + str(count))
print("Total:" + " " + "$" + str(sum(profit_loss)))