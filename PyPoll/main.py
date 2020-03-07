# import modules
from os import path
from csv import DictReader

# declare CSV file location
csvpath = path.join("Resources", "election_data.csv")

# declare text file location
outpath = path.join("Output", "election_results.txt")

# read csv file for parsing
data = DictReader(open(csvpath, 'r', newline=''), delimiter=',')

# declare text file for storing results
output_file = open(outpath, 'w')

# extract header row from csv file
headers = data.fieldnames

# extract list of votes
votes = [ row['Candidate'] for row in data ]

# calculate the number of total votes
totalVotes = len(votes)

# extract unique list of candidates 
nominees = set(votes)

# create a dict of candidate their stats for
# count of votes and percentage of total votes
candidates = { i: { 'votes': votes.count(i), 'percent': round(votes.count(i)/totalVotes * 100, 2) } for i in nominees }

# retrieve the winner of the election (highest percentage of votes)
winner = max(candidates.items(), key=lambda v: v[1]['percent'])

# print total votes to terminal
print('\n=====================================')
print('         ELECTION RESULTS')
print('=====================================\n')
print(f'Total Votes : {totalVotes}\n')

# initialize empty list to store stats
# for writing to file all at once
stats = []

# loop through the candidates
for candidate in candidates:

    # store stats in a variable
    message = f'{candidate} received {candidates[candidate]["percent"]}% of votes for a total of {candidates[candidate]["votes"]} votes.'

    # print current candidate stats to terminal
    print(message)

    # append current stats to the list of `stats`
    stats.append(message+'\n')

# print winner to terminal
message = f'The winner of the election is {winner[0]}!'
print('\n=====================================\n')
print(message.upper())
print('\n=====================================\n')

# write analysis to text file
output_file.write('=====================================\n')
output_file.write('         ELECTION RESULTS\n')
output_file.write('=====================================\n\n')
output_file.write(f'Total Votes : {totalVotes}\n\n')
output_file.writelines(stats)
output_file.write('\n=====================================\n\n')
output_file.write(message.upper() + '\n')
output_file.write('\n=====================================\n')
