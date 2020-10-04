import os
import csv

path = os.path.join('PyBank','Resources', 'budget_data.csv')
change = []
net = 0

with open(path) as budget_file:

    reader = csv.reader(budget_file, delimiter=",")
    header = next(reader)
    count = sum(1 for row in reader)

with open(path) as budget_file:

    reader = csv.reader(budget_file, delimiter=",")
    header = next(reader)

    monthly_profit = [int(profit[1]) for profit in reader]

    first_month = monthly_profit[0]
    previous_month = 0
    
    for i in monthly_profit:
        if i == monthly_profit[0]:
            first_month = monthly_profit[0]
            previous_month = i
        else:
            change.append(i-previous_month)
            previous_month = i
    
    average_change = sum(change) / (count-1)

   

    
        
        

        
        


print("Total Months:" + " " + str(count))
print("Total:" + " " + "$" + str(sum(monthly_profit)))
print("Average Change" + " " + "$" + str(round(average_change, 2)))


