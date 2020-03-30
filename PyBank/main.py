# First I need to import os for operating system Activity 8 Python2
import os
#This grabs and reads the file I need to analyze
import csv 

budget = os.path.join('.','budget_data.csv')

#declare my variables
# The zeros are the starting point for the count
dates= []
months= 0
total_months= []
total_rev = []
average_change= []
pl_change= [0]
greatest_increase= []
greatest_decrease= []

# read the dataset
with open(budget, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    

# I need to figure out the calculations
#total months first
# total_months = len(months) why doesn't this work
    for row in csvfile:
        months +=1
with open(budget, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#find the profits and loss
    for pl in csvreader:
        total_rev.append((int(pl[1])))
        dates.append(pl[0])
    
 #this is for the total print statement
    for row in total_rev:
        total = sum(total_rev)
    
#pl change to calculate the average change
#the pl_change has both [0] because we are doing a list and starting it at 0
with open(budget, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)



    for change in range(len(total_rev)-1):
        pl_change.append(int(total_rev[change + 1])-int(total_rev[change]))
    
    average_change = (sum (pl_change)/85)
# merge the dates and pl change to get the increase/decrease
merge = zip(dates, pl_change)

#Pull the greatest increase and decreas
greatestinc= (max(pl_change))
greatestdec= (min(pl_change))
with open(budget, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)


for last in merge:
        if last[1]== greatestinc:
            greatestinc_date = last[0]
        elif last[1] == greatestdec:
            greatestdec_date = last[0]

#output thank you lord!!!!!
print("Financial Analysis")
print(f"Total Months: {months}")
print(f"Total Revenue: ${total}")
print(f"Average Change:{average_change}")
print(f"Greatest Increase in Profits: {greatestinc_date} (${greatestinc})")
print(f"Greatest Decrease in Profits: {greatestdec_date} (${greatestdec})")