import os
import csv

financial_csv = os.path.join('..','Resources','budget_data.csv')

month_count = 0

def analysis(finanacial_data):
    profit_losses = int(list(financial_data[1]))
    date = str(financial_data[0])
    date_list = int(list(financial_data[0]))

    date_count = len(data_list)

    total += profit_losses
    net_total = total

    average_change = net_total/date_count

    Greatest_Increase = max(profit_losses)
    Greatest_Decrease = min(profit_losses)

    print(f'{date_count}')
    print(f'{net_total}')
    print(f'{average_change}')
    print(f'{Greatest_Increase}')
    print(f'{Greatest_Decrease}')

with open(financial_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        month_count += 1
        analysis
        
print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {month_count}')
