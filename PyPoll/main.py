# Import dependencies
import os
import csv

# Path to collect data from the Resources folder, because this python file is in the same location as the Resources folder, '..' is not needed
vote_count_csv = os.path.join('Resources','election_data.csv')

# Declare the keys and their initial values
voter_count = 0
all_candidates = []
candidate_count = 0
# Found 4 unique candidates from running print(unqiue(all_candidates)) below
candidate1 = 0
candidate2 = 0
candidate3 = 0
candidate4 = 0

# Function for getting each candidate's name without repeating
def unique(candidate_list):
    # Create a list for storing the unique candidate names
    unique_list = []

    # Read through the candidate list, if candidate name is not already in the list, add it
    for candidates in candidate_list:
        if candidates not in unique_list:
            unique_list.append(candidates)

    # End the function and return the result when called 
    return unique_list

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
        # Assign the candidate list to all_candidates
        all_candidates.append(row[2])

# Use the unique function to get a list of candidates 
unique_list = unique(all_candidates)

# Get the count each candidate received
candidate1 = (all_candidates.count(unique_list[0])/voter_count) * 100
candidate2 = (all_candidates.count(unique_list[1])/voter_count) * 100
candidate3 = (all_candidates.count(unique_list[2])/voter_count) * 100
candidate4 = (all_candidates.count(unique_list[3])/voter_count) * 100

print("Election Results")
print("--------------------------------")
print(f'Total Votes: {voter_count:0,.0f}')# the :0,.0f is for converting the number to a easier read
print("--------------------------------")
# Ran this to see how many unqiue candidates in the data: print(unique(all_candidates))
print(unique_list[0])
print(f'{candidate1}')
print(f'{candidate2}')
print(f'{candidate3}')
print(f'{candidate4}')