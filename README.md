# Election_Audit_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of counties where ballots were cast.
3. Calculate the total number of ballots cast in each county.
4. Calculate the percentage of ballots cast in each county.
5. Deterine the county with the largest voter turnout.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code 1.56.2

## Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The counties that received ballots were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson county received 10.5% of the ballots and 38,855 ballots.
  - Denver county received 82.8% of the ballots and 306,055 ballots.
  - Arapahoe county received 6.7% of the ballots and 24,801 ballots.
- The county with the largest voter turnout was:
  - County of Denver which received 82.8% of the ballots and 306,055 ballots.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Candidate Diana DeGette who received 73.8% of the vote and 272,892 votes.

## Summary
While this script was written specifically for assessing a singular multi-county election, the script could be modified to audit results of any election by modifying relevant sections of code to adjust for variances in the regional breakdown of ballots from county to township, municipality, district, etc. and for the number of distinct races being run simultaneously. Such changes would allow for broad utilization of the script to audit elections regardless of the differences.

If utilized for different localities the code could be refactored to change the labels of the output by referencing the header row. In the code we skip the header row using the following code:

```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
header = next(reader)
```
Instead we could put those values in a list and call the necessary value when needed later by indexing the column. Doing so would require something as simple as running a for row loop and breaking after the first iteration while storing the values in a list.

```
column_name_list = []
for row in reader:
  column_name_list.append(row)
  break
```

Then instead of referencing county, presuming the file format is the same or adjusting if it's not, we could simply reference column_name_list[1] utilizing a variable to replace all instances where county is referenced while summarizing/printing. For parsing the actual data the header row would be skipped as normal.

Additionally, the code could easily be refactored to account for multiple votes cast by duplicating the tabulation method and referencing the corresponding column in the CSV file if column headers were used to track specific races similar to how we differentiate between candidates and counties by referencing the column index.

```
        # Get the candidate name from each row.
        candidate_name = row[2]
```

If instead a column was utilized to denote the specific race we could utilize conditionals to check and tabulate each race by creating a separate list and dictionary for each office up for election. Ultimately it depends on the nature of the layout of the data file utilized to track the results but such changes would be minor to account for any variance. As designed the number of counties (or corresponding locality) and candidates are not hard coded and as such it would be easy to transition to elections with a differing number of sources of ballots and candidates or even candidate offices for each election.
