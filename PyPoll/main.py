# Import dependencies
import os
import csv

# Path to collect data from the Resources folder, because this python file is in the same location as the Resources folder, '..' is not needed
vote_count_csv = os.path.join('Resources','election_data.csv')

# Declare the keys and their initial values
voter_count = 0

# Read in the csv file
with open(vote_count_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # Add 1 after each voter
        voter_count += 1

print("Election Results")
print("--------------------------------")
print(f'Total Votes: {voter_count:0,.0f}')# the :0,.0f is for converting the number to a easier read
print("--------------------------------")