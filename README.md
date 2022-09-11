# Election_Analysis

## Overview of Election Audit
Using data provided by a Colorado Board of Elections to audit a recent local congressional election.

1. How many votes were cast in this congressional election?
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
3. Which country had the largest number of votes?
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
5. Which candidate won the election, what was their vote count, and what was their percentage of total votes?

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.71.0

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election
- County Votes:
     - Jefferson:  10.5% (38,855)
     - Denver:  82.8% (306,055)
     - Arapahoe:  6.7% (24,801)
- Largest County Turnout: Denver
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 272,892 votes which was 73.8% of the vote.

## Election Audit Summary

### Benefits of Current Script
The script used in analyzing the data provided will be useful for any election. As long as the data is formatted in a csv file with the county in the second row or first index and the candidate in the third row or second index. 

### Modifications

My understanding of this script leads me to believe that the following code can be added to further audit the data and return an error message to alert the user of duplicate Ballot' ID's. There is a chance that because I am iterating through each row individually, this may not actually catch duplicates if the Ballot ID's are not in order. 

In line 30, initialize a list to hold the Ballot ID's:
insert mod_1_ballot_id_options


In line 70, get the Ballot ID from each row.
insert mod_1_ballot_id


In lines 103 to 105, write an if statement to print the error message if the ballot ID is found in the list. 
insert mod_1_if_statement







    

