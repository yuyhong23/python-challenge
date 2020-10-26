import os
import csv

financial_csv = os.path.join('..','Resources','budget_data.csv')

month_count = 0
net_total_profit = 0

with open(financial_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        month_count += 1
        profit = int(row[1])
        net_total_profit = net_total_profit + profit
        
print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${net_total_profit:0,.0f}')
