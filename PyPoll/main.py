# import the os module
import os

# Module for reading csv file
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')


#Create lists to
Total_votes = 0
candidate_votes = {}


# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip header labels
    csv_header = next(csv_reader)

    #Read through each row of data after the header
    for row in csv_reader:

        #Create total votes variable
        Total_votes += 1
        candidate = row[2]

        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    #Find percentage
    winner = ''
    winning_count = 0
    percentage_candidate = {}

    for candidate, votes in candidate_votes.items():
        percentage = (votes / Total_votes) * 100
        percentage_candidate[candidate] = percentage

     #Finding the winner
        if votes > winning_count:
            winning_count = votes
            winner = candidate


#Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(Total_votes)}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentage_candidate[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Specify the file to write to
output_file = os.path.join("Analysis", "election_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w', newline='') as cvsfile:
    writer = csv.writer(cvsfile, delimiter=',')

     # Write the header and separator lines as lists
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
   
   # Write total votes
    writer.writerow([f"Total Votes: {str(Total_votes)}"])

    writer.writerow(["-------------------------"])

   # Write candidate votes
    for candidate, votes in candidate_votes.items():
        writer.writerow([f"{candidate}: {percentage_candidate[candidate]:.3f}% ({votes})"]) 

    writer.writerow(["-------------------------"])
    
    # Write the winner
    writer.writerow([f"Winner: {winner}"])
    
    writer.writerow(["-------------------------"])





   

  

  