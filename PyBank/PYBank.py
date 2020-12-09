# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:44:47 2020

@author: abroeren
"""
import os
import csv
import sys

CountRow = 0
MonthsTotal = 0
MonthlyChange = 0
AverageChange = 0
TotalChange = 0
PreviousRow = 0
GreatestIncrease = 0
GreatestDecrease = 0

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    csv_header = next(csvreader)
    # print(f'csvheader: {csv_header}')
    
    for row in csvreader:
        if row[0] == 'Jan-2010':
            PreviousRow = int(row[1])
        CountRow = CountRow + 1
        MonthsTotal = MonthsTotal +int(row[1])
        
        MonthlyChange = int(row[1]) - PreviousRow
        # print(row[0],row[1], MonthlyChange)
        TotalChange = TotalChange + MonthlyChange
        PreviousRow = int(row[1])

        if GreatestIncrease < MonthlyChange:
            GreatestIncrease = MonthlyChange
            GreatestIncreaseMonth = row[0]
            
        if GreatestDecrease > MonthlyChange:
            GreatestDecrease = MonthlyChange
            GreatestDecreaseMonth = row[0]
        
AverageChange = TotalChange / (CountRow - 1)

# Print to console

print("Financial Analysis\n"
      "-------------------------------------------")
print("Total Months: ", CountRow)
MonthsTotal = "${:.0f}".format(MonthsTotal)
print("Total: ", MonthsTotal)
AverageChange = "${:.2f}".format(AverageChange)
print("Average Change: ",AverageChange)
GreatestIncrease = "(${:.0f})".format(GreatestIncrease)
print("Greatest Increase in Profits: ", GreatestIncreaseMonth, GreatestIncrease)
GreatestDecrease = "(${:.0f})".format(GreatestDecrease)
print("GreatestDecrease in Profits: ", GreatestDecreaseMonth, GreatestDecrease)

# Print to Text file
stdoutOrigin=sys.stdout
txtPath = os.path.join("Analysis", "financial-analysis.txt")
sys.stdout = open(txtPath, "w")

print("Financial Analysis")
print("-------------------------------------------")
print("Total Months: ",CountRow)
print("Total: ",MonthsTotal)
print("Average Change: ", AverageChange)
print("Greatest Increase in Profits: ",GreatestIncreaseMonth, GreatestIncrease)
print("Greatest Decrease in Profits: ",GreatestDecreaseMonth,GreatestDecrease)

sys.stdout.close()
sys.stdout=stdoutOrigin


