# import the necessary modules
import os
import csv

# add filepath
csvpath = os.path.join('Resources', 'budget_data.csv')

# lists to store data
months = []
profit_loss = []
change = []

# read file using csv module
with open(csvpath) as file:
    csv_reader = csv.reader(file, delimiter=',')

    csv_header = next(csv_reader)
    #print(f'CSV header: {csvheader}')

    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))


for i in range(len(profit_loss)-1):
    change.append(profit_loss[i+1]-profit_loss[i])

change_months = months[1:]
months_and_change = list(zip(change, change_months))

Total_months = len(months)
Total = '${}'.format(sum(profit_loss))
Average_Change = '${:.2f}'.format(sum(change) / len(change))
max_change = '{} (${})'.format(max(months_and_change)[1], max(months_and_change)[0])
min_change = '{} (${})'.format(min(months_and_change)[1], min(months_and_change)[0])

# write the results to a text file
text_heading = ['Financial Analysis']
with open('analysis/analysis.txt', 'w') as f:
    f.writelines(text_heading)

text = [' ', '----------------------------',
                f'Total Months: {Total_months}',
                f'Total: {Total}',
                f'Average Change: {Average_Change}',
                f'Greatest Increase in Profits: {max_change}',
                f'Greatest Decrease in Profits: {min_change}'
        ]

with open('analysis/analysis.txt', 'a') as f:
    f.write('\n'.join(text))

# print the analysis
print('Total Months:',Total_months)
print('Net Total:' , Total)
print('Average Change:', Average_Change)
print('Greatest Increase in Profits:',max_change)
print('Greatest Decrease in Profits:',min_change)