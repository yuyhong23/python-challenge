import os
import csv

financial_csv = os.path.join('..','Resources','budget_data.csv')

month_count = 0

print("Financial Analysis")
print("------------------------------------------")

with open(financial_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        month_count += 1

print(f'Total Months: {month_count}')