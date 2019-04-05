import os
import csv

#Open and read csv
#print(os.getcwd())
csvpath = os.path.join('Resources', 'budget_data.csv')

months = 0
bankDic = {}

with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  
  csv_header = next(csvreader)

#Find Months and Add to Dic as Keys
  for row in csvreader:

      months = months+1

      bankDic[row[0]] = int(row[1])

#Calculate Total Profit/Loss
      values = bankDic.values()
      netTotal = sum(values)

#Calculate Average Change
      totalItems = len(bankDic)
      averageChange = round(netTotal / totalItems, 2)

#Calculate Greatest Profit
      maxProfit = max(values)
      maxDate = list(bankDic.keys())[list(bankDic.values()).index(maxProfit)]

#Calculate Greatest Loss
      minLoss = min(values)
      minDate = list(bankDic.keys())[list(bankDic.values()).index(minLoss)]

#Print Data in Terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {months} ")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {maxDate} ({maxProfit})")
print(f"Greatest Decrease in Profits: {minDate} ({minLoss})")

#Write and Export File

output_file = os.path.join("PyBank_Analysis.csv")

with open(output_file, "w", newline="") as xfile:

    column_title_row = "Data Type, Value" + '\n'
    xfile.write(column_title_row) 
    xfile.write("Total Months:, " + str(months) + '\n')
    xfile.write("Total:, " + "$" + str(netTotal) + '\n')
    xfile.write("Average Change:, " + "$" + str(averageChange) + '\n')
    xfile.write("Greatest Increase in Profits:, " + str(maxDate) + " (" + str(maxProfit) + ")" + '\n')
    xfile.write("Greatest Decrease in Profits:, " + str(minDate) + " (" + str(minLoss) + ")" + '\n')

    xfile.close()