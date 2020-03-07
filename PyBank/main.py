# import modules
from os import path
from csv import DictReader

# declare CSV file location
csvPath = path.join('Resources', 'budget_data.csv')

# declare text file location
outpath = path.join('Output', 'financial_results.txt')

# read csv file for parsing
csvreader = DictReader(open(csvPath, 'r', newline=''))

# declare text file for storing results
output_file = open(outpath, 'w')

# extract header row from csv file
headers = csvreader.fieldnames

# declare new columnn
new_header = 'Monthly Change'

# add new column to current list of headers
headers.append(new_header)

# initialize the counters and variables for comparison
totalMonths = 0
totalPL = 0
previousPL = 0
avgChange = 0

# initialize empty list for storing rows for analysis
changeList = []

# loop through each row of CSV data
for row in csvreader:

    # store current row's `Profit/Losses` value
    currentPL = float(row['Profit/Losses'])

    # store current row's `Date`
    currentDT = row['Date']

    # calculate and store the change of current row's
    # `Prices/Losses` value from prior month
    currentChg = round(currentPL - previousPL)

    # update current row with new column `Monthly Change`
    row.update({ new_header: currentChg })
    
    # update list of changes for further analysis
    changeList.append(row)

    # store current `Prices/Losses` value for comparison by next row
    previousPL = currentPL

    # increase total months counter by 1
    totalMonths += 1

    # add current row's `Prices/Losses` value to total counter
    totalPL = totalPL + round(currentPL)

# retrieve the greatest amount of change and date from the list `changeList`
greatestInc = max(changeList, key=lambda x: x[new_header])

# retrieve the least amount of change and date from the list `changeList`
greatestDec = min(changeList, key=lambda x: x[new_header])

# sum the values of monthly change in list `changeList`
totalChg = sum([change[new_header] for change in changeList])

# calculate the average change
avgChange = round((totalChg - changeList[0][new_header]) / (len(changeList)-1),2)

# print analysis to terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: { totalMonths }')
print(f'Total: $ { totalPL }')
print(f'Average Change: $ { avgChange }')
print(f'Greatest Increase in Profits: {greatestInc["Date"]} (${greatestInc[new_header]})')
print(f'Greatest Decrease in Profits: {greatestDec["Date"]} (${greatestDec[new_header]})')
print()

# write analysis to text file
output_file.write('Financial Analysis\n')
output_file.write('----------------------------\n')
output_file.write(f'Total Months: { totalMonths }\n')
output_file.write(f'Total: $ { totalPL }\n')
output_file.write(f'Average Change: $ { avgChange }\n')
output_file.write(f'Greatest Increase in Profits: {greatestInc["Date"]} (${greatestInc[new_header]})\n')
output_file.write(f'Greatest Decrease in Profits: {greatestDec["Date"]} (${greatestDec[new_header]})\n\n')
