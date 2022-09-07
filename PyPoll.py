
#Add our dependencies
import csv
from distutils import text_file
import os

#Assign a variable for the file to load the path
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file
# with open(file_to_load) as election_data:

#     #print the file object
    # print(election_data)

    #To do: perform analysis

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# #write some data to the file.
# outfile.write("Hello World")

# #close the file
# outfile.close

# # Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

   # Write three counties to the file
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson") OR
    # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
        # for row in file_reader:
        #     print(row)

    #  #Print the first row in the CSV file.
    #     for row in file_reader:
    #         print(row[0])
    









#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote