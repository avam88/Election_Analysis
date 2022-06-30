import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

#Create candidate name variable list
candidate_options = []

# declaring our candidate votes dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add candidate name to candidate options
            candidate_options.append(candidate_name)

            # Tracking candidate vote counts
            candidate_votes[candidate_name] = 0

        # increment candidate votes
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # retrieve vote cont of a candidate.
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of votes to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    

    # determine whether candidate has majority count
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes
        winning_percentage = vote_percentage

        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
