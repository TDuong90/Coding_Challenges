import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0
total = 0

total_month_change = 0
month_change = 0
average_change = 0

previous_lost_profit = 0
increase = 0
increase_month = ""
decrease = 0
decrease_month = ""

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        total_months = total_months + 1
        total = total + int(row[1])

        if total_months > 1:
         month_change = int(row[1]) - previous_lost_profit

        total_month_change = total_month_change + month_change

        previous_lost_profit = int(row[1])

        if month_change > increase:
            increase = month_change
            increase_month = row[0]
        if month_change < decrease:
            decrease = month_change
            decrease_month = row[0]
        

average_change = total_month_change / (total_months - 1)

print(f"Financial Analysis")
print(f"----------------------------")    
print(f"Total Months: {total_months}")
print(f"Total: $ {total}")
print("Average Change: $" + str(format(average_change,'.2f')))
print(f"Greatest Increase in Profits: {increase_month} (${increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")

with open("PyBank.txt", 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: $ {total}\n")
    txtfile.write(f"Average Change: $" + str(format(average_change,'.2f')))
    txtfile.write(f"Greatest Increase in Profits: {increase_month} (${increase})")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")