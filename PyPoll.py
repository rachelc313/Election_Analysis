# Add our dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save a file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate options and candidate votes
candidate_options = []


#Declare the empty dictionary
candidate_votes = {}

#Wining Candidate and Winning Count tracker
#Declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""

#Declare a variable for the "winning count" equal to zero
winning_count = 0

#Declare a variable for the "winning percentage" equal to zero
winning_percentage = 0

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

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

  election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")

  print(election_results, end="")
  
  #save the final vote count to the text file.
  txt_file.write(election_results)



  #Determine percentage of votes

  #1For loop to iterate through candidate options list - gets candidate name
  for candidate_name in candidate_votes:

    #2Use the for loop variable to retrieve the votes of the candidate from the candidate votes dict
    votes = candidate_votes[candidate_name]

    #3 Calculate the percentage of the vote count
    vote_percentage = float(votes) / float(total_votes) * 100

    # #Print each candidate and the percentage of vote using f string format
    # print(f"{candidate_name} received {vote_percentage: .1f}% of the vote.")


  #Determine if the vote count that was calculated is greater than the winning_count variable
    if (votes > winning_count) and (vote_percentage > winning_percentage):

      #if true set winning count equal to votes
      winning_count = votes

      #vote percentage
      winning_percentage = vote_percentage

      #set the winning candidate equal to the candidate's name
      winning_candidate = candidate_name

    #Print each candidate and the percentage of vote using f string format
    # print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

    winning_candidate_summary = (
      f"---------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: ({winning_count:,})\n"
      f"Winning Percentage: {winning_percentage: .1f}%\n"
      f"---------------------------\n")

    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

  #Print each candidate, their voter count, and percentage to the terminal
    print(candidate_results)
  
  #Save the candidate results to the text file.
    txt_file.write(candidate_results)

  # print(winning_candidate_summary)