import os
import csv

path = os.path.join('PyBank','Resources', 'budget_data.csv')

monthly_profit = []
month_list = []
change = []

with open(path) as budget_file:

    reader = csv.reader(budget_file, delimiter=",")
    header = next(reader)
    count = sum(1 for row in reader)

with open(path) as budget_file:

    reader = csv.reader(budget_file, delimiter=",")
    header = next(reader)

    for row in reader:
        monthly_profit.append(int(row[1]))
        month_list.append(str(row[0]))
    

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
    
    max_index = change.index(max(change))
    min_index = change.index(min(change))

    max_month = str(month_list[max_index + 1])
    max_change = ("$" + str(max(change)))

    min_month = str(month_list[min_index + 1])
    min_change = ("$" + str(min(change)))



print("Financial Analysis")
print("------------------------")
print("Total Months:" + " " + str(count))
print("Total:" + " " + "$" + str(sum(monthly_profit)))
print("Average Change" + " " + "$" + str(round(average_change, 2)))
print("Greatest Increase in Profit:" + " " + max_month + " " + "(" + max_change + ")")
print("Greatest Decrease in Profit:" + " " + min_month + " " + "(" + min_change + ")")

output = os.path.join("Pybank","Analysis","budget_analysis.txt")

with open(output, 'w') as txt_file:
    
    txt_file.write("Financial Analysis" + os.linesep)
    txt_file.write("------------------------" + os.linesep)
    txt_file.write("Total Months:" + " " + str(count) + os.linesep)
    txt_file.write("Total:" + " " + "$" + str(sum(monthly_profit)) + os.linesep)
    txt_file.write("Average Change" + " " + "$" + str(round(average_change, 2)) + os.linesep)
    txt_file.write("Greatest Increase in Profit:" + " " + max_month + " " + "(" + max_change + ")" + os.linesep)
    txt_file.write("Greatest Decrease in Profit:" + " " + min_month + " " + "(" + min_change + ")" + os.linesep)
    
    


