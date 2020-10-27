# Import the os module
import os
# Module for reading csv file
import csv

# Path to collect data from the Resources folder, because this python file is in the same location as the Resources folder, '..' is not needed
financial_csv = os.path.join('Resources','budget_data.csv')

# Declare the keys and their initial values
month_count = 0
net_total_profit = 0
last_profit = 0
change = []
total_average_change = 0
average_change_month_count = 0

# Read in the csv file
with open(financial_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # Add 1 after each month
        month_count += 1
        
        # Identity the data to use for month and profit
        month = row [0]
        profit = int(row[1])

        # If the month count is equal to 1, set the last profit as profit
        if month_count ==1:
            last_profit = profit
        # If the month count is not equal to 1, subtract the current value by the current value, and store that difference in a list call "change"
        else:
            change.append(profit-last_profit)
            # Update the last profit value
            last_profit = profit 
        
        # Create and define a function called "average" to calculate the sum of all the values in the "change" list
        def average(change): 
            total_change = 0
            for value in change:
                total_change += value
            return total_change

        # Calculate the net total profit by adding all the profits/losses
        net_total_profit = net_total_profit + profit
    
    # To get the number of month for the average change, minus 1 because the first difference is from the second value subtracting the first value
    average_change_month_count = month_count-1
    # Calculating the total of the changes in profits/losses
    total_average_change = average(change)/average_change_month_count 

# Print out the result
print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${net_total_profit:0,.0f}') # the :0,.0f is for converting the number to currency
print(f'Average Change: ${total_average_change:0,.02f}') # the :0,.02f is for converting the number to currency with two decimal points