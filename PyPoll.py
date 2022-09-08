
#Add our dependencies
import csv
from distutils import text_file
import os

#Assign a variable for the file to load the path
file_to_load = 'Resources/election_results.csv'

#Assign a variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []

#Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    

    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any exiting candidate...
        if candidate_name not in candidate_options:

            #Add it to the list of candidates
            candidate_options.append(candidate_name)



# Print the candidate list.
print(candidate_options)

   
    









#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote