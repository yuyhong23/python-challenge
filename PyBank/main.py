import os
import csv

financial_csv = os.path.join('Resources','budget_data.csv')

month_count = 0
net_total_profit = 0
last_profit = 0
change = []
total_average_change = 0
average_change_month_count = 0

with open(financial_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        month_count += 1

        profit = int(row[1])
        month = row [0]
        if month_count ==1:
            last_profit = profit
        else:
            change.append(profit-last_profit)
            last_profit = profit 
        
        def average(change): 
            total_change = 0
            for value in change:
                total_change += value
            return total_change

        net_total_profit = net_total_profit + profit
    
    average_change_month_count = month_count-1
    total_average_change = average(change)/average_change_month_count 

print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${net_total_profit:0,.0f}')
print(f'Average Change: ${total_average_change:0,.02f}')