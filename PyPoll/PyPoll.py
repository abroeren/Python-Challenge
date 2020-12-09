# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:44:47 2020

@author: abroeren
"""
import os
import csv
import sys

# Variables
TotalVotes = 0
KhanCount = 0
CorreyCount = 0
LiCount = 0
OTooleyCount = 0
KhanPercent = 0
CorreyPercent = 0
LiPercent = 0
OTooleyPercent = 0
Winner = 0

# Import CVS File
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f'csvheader: {csv_header}')

    for row in csvreader:
        TotalVotes = TotalVotes + 1
        if row[2] == "Khan":
            KhanCount = KhanCount +1
        elif row[2] == "Correy":
            CorreyCount = CorreyCount +1
        elif row[2] == "Li":
            LiCount = LiCount +1
        else:
            OTooleyCount = OTooleyCount +1
            
    KhanPercent = (KhanCount / TotalVotes)
    CorreyPercent = (CorreyCount / TotalVotes)
    LiPercent = (LiCount / TotalVotes)
    OTooleyPercent = (OTooleyCount / TotalVotes)
    
    Winner = max(KhanCount,CorreyCount,LiCount,OTooleyCount)
    
    if Winner == KhanCount:
        WinnerName = "Khan"
    elif Winner == CorreyCount:
        WinnerName = "Correy"
    elif Winner == LiCount:
        Winnername = "Li"
    else:
        Winnername == "O'Toole"

print("Election Results")
print("--------------------------")
print("Total Votes: ", TotalVotes)
print("--------------------------")
KhanPercent = "{:.3%}".format(KhanPercent)
KhanCount = "({:.0f})".format(KhanCount)
print("Khan: ", KhanPercent, KhanCount)
CorreyPercent = "{:.3%}".format(CorreyPercent)
CorreyCount = "({:.0f})".format(CorreyCount)
print("Correy: ", CorreyPercent, CorreyCount)
LiPercent = "{:.3%}".format(LiPercent)
LiCount = "({:.0f})".format(LiCount)
print("Li: ", LiPercent, LiCount)
OTooleyPercent = "{:.3%}".format(OTooleyPercent)
OTooleyCount = "({:.0f})".format(OTooleyCount)
print("O'Tooley: ", OTooleyPercent, OTooleyCount)
print("--------------------------")
print("Winner: ", WinnerName)
    
   
#Print to Text file

stdoutOrigin=sys.stdout
txtPath = os.path.join("Analysis", "Election_Results.txt")
sys.stdout = open(txtPath, "w")

print("Election Results")
print("--------------------------")
print("Total Votes: ", TotalVotes)
print("--------------------------")
print("Khan: ", KhanPercent, KhanCount)
print("Correy: ", CorreyPercent, CorreyCount)
print("Li: ", LiPercent, LiCount)
print("O'Tooley: ", OTooleyPercent, OTooleyCount)
print("--------------------------")
print("Winner: ", WinnerName)

sys.stdout.close()
sys.stdout=stdoutOrigin
        