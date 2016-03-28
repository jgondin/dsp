"""
The football.csv file contains the results from the English 
Premier League.
The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total 
number of goals scored for and against each team in that season
(so Arsenal scored 79 goals against opponents, and had 36 goals
scored against them). Write a program to read the file, then
print the name of the team with the smallest difference in ‘for’
and ‘against’ goals.

The below skeleton is optional.  You can use it or you can
write the script with an approach of your choice.
"""

import csv

def read_data(data):
    # COMPLETE THIS FUNCTION
    f = open(data)
    return(list(csv.reader(f)))

def get_min_score_difference(parsed_data):
    # COMPLETE THIS FUNCTION
    diff = []
    for i in range(len(data)) :
        diff.append((int(data[6]) - int(data[i][5])))
    return(max(diff))

def get_team(index_value, parsed_data):
    # COMPLETE THIS FUNCTION
        
