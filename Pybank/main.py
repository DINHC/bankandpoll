import os
import csv
file_path = os.path.join("Resources","budget_data.csv") 

total_months = 0
total_profit_loss = 0 #profit/loss (change name maybe?)
value = 0
change = 0
dates = []
profits = []


with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")
    csv_header = next(csv_reader)
    file_to_output = "budget_analysis.txt"
    first_row = next(csv_reader)

    total_months = total_months + 1
   
    total_profit_loss = total_profit_loss + int(first_row[1])
  
    value = int(first_row[1])
      
      
    for row in csv_reader:
        
        total_months = total_months + 1 
        change = int(row[1])-value
        total_profit_loss = total_profit_loss + int(row[1]) 
        profits.append((row[1])) 
        value = int(row[1])
        dates.append(row[0])  

        
        average = sum(profits)/len(profits) # error here regarding operands check in eralier line if there is misspelling

        Greatest_Decrease = min(profits)
        Lowest_Index = profits.index(Greatest_Decrease)
        Lowest_Date = dates[Lowest_Index]

        Greatest_Increase = max(profits)
        Greatest_Index = profits.index(Greatest_Increase)
        Greatest_Date = dates[Greatest_Index]



print("Financial Analysis")
print("------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit_loss)}")
print(f"Average Change: ${str(round(average,2))}")
print(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})")
print(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})")

        
os.getcwd


    


