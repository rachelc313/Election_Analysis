# Add our dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save a file to a path
file_to_save = os.path.join("anaysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate options and candidate votes
candidate_options = []


#Declare the empty dictionary
candidate_votes = {}

#Open the election resultsread the file
with open(file_to_load) as election_data:

  #read the file
  file_reader = csv.reader(election_data)

  #Read the header row
  headers = next(file_reader)

  #Print each row in the CSV file with a for loop
  for row in file_reader:

    #Add to the total vote count
    total_votes += 1

    #Print the candidate name from each row
    candidate_name = row[2]

    #If statement here for starting the list of candidate names
    if candidate_name not in candidate_options:
      
      #In the if statement

      #Add the candidate name to the candidate list
      candidate_options.append(candidate_name)

      #Begin tracking that candidate's vote count.
      candidate_votes[candidate_name] = 0

    #Add a vote to that candidate's vote count
    candidate_votes[candidate_name] += 1

    #In line with the if statement - in the for loop
  #In line with the for loop - in the with open statement
#in line with "with open" - flush with left margin

#Determine percentage of votes

#1For loop to iterate through candidate options list - gets candidate name
for candidate_name in candidate_votes:

  #2Use the for loop variable to retrieve the votes of the candidate from the candidate votes dict
  votes = candidate_votes[candidate_name]

  #3 Calculate the percentage of the vote count
  vote_percentage = float(votes) / float(total_votes) * 100

  #Print each candidate and the percentage of vote using f string format
  print(f"{candidate_name} received {vote_percentage: .1f}% of the vote.")