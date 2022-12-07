# import the necessary modules
import os
import csv

# add filepath
csvpath = os.path.join('Resources', 'election_data.csv')

# lists to store data
ballot_id = []
county = []
candidate = []

# read file using csv module
with open(csvpath) as file:
    csv_reader = csv.reader(file, delimiter=',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# analyse the required outputs
Total_votes = len(ballot_id)
Charles_votes = candidate.count('Charles Casper Stockham')
Diana_votes = candidate.count('Diana DeGette')
Raymon_votes = candidate.count('Raymon Anthony Doane')
Charles_votes_percent = '{:.3f}'.format(Charles_votes * 100 / (Total_votes))
Diana_votes_percent = '{:.3f}'.format(Diana_votes * 100 / (Total_votes))
Raymon_votes_percent = '{:.3f}'.format(Raymon_votes * 100 / (Total_votes))

Charles_data = '{}% ({})'.format(Charles_votes_percent, Charles_votes)
Diana_data = '{}% ({})'.format(Diana_votes_percent, Diana_votes)
Raymon_data = '{}% ({})'.format(Raymon_votes_percent, Raymon_votes)

# create a list of candidates and their votes
candidate_votes = list(zip([Charles_votes,Diana_votes,Raymon_votes], ['Charles Casper Stockham', 'Diana DeGette','Raymon Anthony Doane']))
winner = max(candidate_votes)[1]

# write the results to a text file
text_heading = ['Election Results']
with open('analysis/analysis.txt', 'w') as f:
    f.writelines(text_heading)

text = [' ', '----------------------------',
                f'Total Votes: {Total_votes}',
                '----------------------------',
                f'Charles Casper Stockham: {Charles_data}',
                f'Diana DeGette: {Diana_data}',
                f'Raymon Anthony Doane: {Raymon_data}',
                '----------------------------',
                f'Winner: {winner}',
                '----------------------------'
        ]

with open('analysis/analysis.txt', 'a') as f:
    f.write('\n'.join(text))

# print the results
print('Election Results')
print('----------------------------')
print('Total Votes:', Total_votes)
print('----------------------------')
print('Charles Casper Stockham:', Charles_data)
print('Diana DeGette:', Diana_data)
print('Raymon Anthony Doane:', Raymon_data)
print('----------------------------')
print('Winner:', winner)
print('----------------------------')