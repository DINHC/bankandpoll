import os
import csv
filepath = os.path.join("..", "Pybank","budget_data.csv") 

total_months = 0
total_profit_loss = 0 #profit/loss (change name maybe?)
value = 0
change = 0
dates = []
profits = []


with open("budget_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")
    csv_header = next(csv_reader)
    file_to_output = "budget_analysis.txt"


    total_months = total_months + 1
   
    total_profit_loss = total_profit_loss + int(first_row[1])
  
    value = int(first_row[1])
      
      
       for row in csv_reader:
        
        total_months = total_months + 1 
        change = int(row[1])-value
        total_profit_loss = total_profit_loss + int(row[1]) 
        profits.append(row[1]) 
        value = int(row[1])
        dates.append(row[0])  

        average = sum(profits)/len(profits)

        Greatest_Decrease = min(profits)
        Lowest_Index = profits.index(Greatest_Decrease)
        Lowest_Date = dates(Lowest_Index)

        Greatest_Increase = max(profits)
        Greatest_Index = profits.index(Greatest_Increase)
        Greatest_Date = dates(Greatest_Index)




        


    


