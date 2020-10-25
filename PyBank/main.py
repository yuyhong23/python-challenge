import os
import csv

financial_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data.csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        