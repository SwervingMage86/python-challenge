#Import Modules
import os
import csv

#Declare file path
path = os.path.join('PyBank','Resources', 'budget_data.csv')

#Define needed lists
monthly_profit = []
month_list = []
change = []

#Read file
with open(path) as budget_file:
    reader = csv.reader(budget_file, delimiter=",")

    #Skip header
    header = next(reader)

    #Count number of rows for total month count    
    count = sum(1 for row in reader)

#Read file...again
with open(path) as budget_file:
    reader = csv.reader(budget_file, delimiter=",")

    #Skip header...again
    header = next(reader)

    #Loop through rows to seperate data into two different lists
    for row in reader:
        monthly_profit.append(int(row[1]))
        month_list.append(str(row[0]))
    
    #Determine value of the first month's profit/loss
    first_month = monthly_profit[0]

    #Define variable for use later
    previous_month = 0
    
    #Loop through monthly profit list to determine month to month change
    for i in monthly_profit:
        if i == monthly_profit[0]:
            first_month = monthly_profit[0]
            previous_month = i

        #Append monthly change values to seperate list
        else:
            change.append(i-previous_month)
            previous_month = i

        #Determine average change
        average_change = sum(change) / (count-1)

    #Find the index values of largest increase and decrease in monthly change
    max_index = change.index(max(change))
    min_index = change.index(min(change))

    #Match Largest increase and decrease to date(add +1 because there is no first month change)
    #Assigned value as string to a variable
    max_month = str(month_list[max_index + 1])
    max_change = ("$" + str(max(change)))

    min_month = str(month_list[min_index + 1])
    min_change = ("$" + str(min(change)))


#Print outcomes in terminal
print("Financial Analysis")
print("------------------------")
print("Total Months:" + " " + str(count))
print("Total:" + " " + "$" + str(sum(monthly_profit)))
print("Average Change" + " " + "$" + str(round(average_change, 2)))
print("Greatest Increase in Profit:" + " " + max_month + " " + "(" + max_change + ")")
print("Greatest Decrease in Profit:" + " " + min_month + " " + "(" + min_change + ")")

#Output values to a text file
output = os.path.join("Pybank","Analysis","budget_analysis.txt")

with open(output, 'w') as txt_file:
    
    txt_file.write("Financial Analysis" + os.linesep)
    txt_file.write("------------------------" + os.linesep)
    txt_file.write("Total Months:" + " " + str(count) + os.linesep)
    txt_file.write("Total:" + " " + "$" + str(sum(monthly_profit)) + os.linesep)
    txt_file.write("Average Change" + " " + "$" + str(round(average_change, 2)) + os.linesep)
    txt_file.write("Greatest Increase in Profit:" + " " + max_month + " " + "(" + max_change + ")" + os.linesep)
    txt_file.write("Greatest Decrease in Profit:" + " " + min_month + " " + "(" + min_change + ")" + os.linesep)
    