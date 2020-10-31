# python-challenge

Data and instruction provided by UC Berkeley Extension Data Analytics Bootcamp.

Two Python Challenges: PyBank and PyPoll.

*PyBank Instruction:*

    Your task is to create a Python script that analyzes the records to calculate each of the following:
        - The total number of months included in the dataset
        - The net total amount of "Profit/Losses" over the entire period
        - The average of the changes in "Profit/Losses" over the entire period
        - The greatest increase in profits (date and amount) over the entire period
        - The greatest decrease in losses (date and amount) over the entire period
        - In addition, your final script should both print the analysis to the terminal and export a text file with the results.

*PyPoll Instruction:*

    You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
        - The total number of votes cast
        - A complete list of candidates who received votes
        - The percentage of votes each candidate won
        - The total number of votes each candidate won
        - The winner of the election based on popular vote.
        - In addition, your final script should both print the analysis to the terminal and export a text file with the results.

**Process and Credits**

My first assignment creating scripts in Python. I used class materials and outside resources for references, asked Bootcamp's Learning Assistant App for help and attended instruction's office hour to complete this assignment.

*PyBank*

1. I used this website (http://publicatodo.co/Detalles/3311/Count-how-many-lines-are-in-a-CSV-Python-) for reference to get the month count.
2. I attended office hour and asked for some tips on finding the total amount of "Profit/losses" over the entire period. The instructor gave some very helpful tips: declaring keys which will be used later and setting up if statement for getting the average change (calculate the change and update the last profit). Instructor also told us about a way to format the float to currency ":0,.0f", and then I looked it up and found this website (https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python) which gave me more detailed explaination on how to use it.
3. I was having trouble exporting a text file with the results, I first searched online and found this website for reference (https://www.codegrepper.com/code-examples/python/python+create+text+file), but I couldn't understand it well, so I asked for help from the Learning Assistant App. The assistant explained to me by pointing out the mistakes I had and gave some suggestions to resolve the issues:1)use text.writelines(...) and 2)only one set of quotation marks are needed when exporting the results to a text file.

*PyPoll*

1. I was having a hard time figuring out how to get a complete list of candidates, so I attended another office hour and asked for some tips to get started. Instructor showed me that I need to declare a list at the beginning and then fill up that list with candidates data from the csv. He was also explaining to another student who asked for help, and gave us a mini lesson on how to get the count for the candidates. He showed us the key and value function, which I used later on in the assignment.
2. I used these websites (https://www.geeksforgeeks.org/python-get-unique-values-list/) (https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/)(https://www.geeksforgeeks.org/python-return-statement/) as references to set up the unique function for finding the a list of candidates.
3. I used this website (https://www.guru99.com/python-list-count.html) as reference for using the count function to find each candidate's vote count.
4. I used this webiste (https://howtodoinjava.com/python/examples/max-min/) as reference for using the max function to find the maximum vote count.
5. I used this website (https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary/8023329) as reference to identifying the name of the candidate with the maximum vote count in a dictionary (this is how I used it in my scripts: print(f'Winner: {list(candidateNcount.keys())[list(candidateNcount.values()).index(winner_count)]}')).

