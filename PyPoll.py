# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes eah candidate won
# 5. The winner of the election based on the popular results

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initalize variables needed.
total_votes = 0
candidate_option = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Skip the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_option:
            # Add the candidate name to the candidate list.
            candidate_option.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidates count.
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote ount to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #3. Print relevant information.
    # print(candidate_option)
    # print(candidate_votes)
    # print(total_votes)
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        if votes > winning_count and vote_percentage > winning_percentage:
            # 2. If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # To do: print ou tthe winning candidate, vote count, and percentage to terminal.
    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)