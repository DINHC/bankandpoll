import os
import csv
filepath = os.path.join("..", "Pybank","budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []


with open("budget_data.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    file_to_output = "budget_analysis.txt"


       for row in csv_reader:
        
        total_months = total_months + 1  #
        
        total_revenue = total_revenue + int(row[1]) 
        revenue.append(row[1]) 
        date.append(row[0])  