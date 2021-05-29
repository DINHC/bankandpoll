import os
import csv
file_path = os.path.join("Resources","budget_data.csv") 

total_months = 0
total_profit_loss = 0 #profit/loss (change name maybe?)
month_amount = 0
monthly_change = 0
dates = []
profits = []


with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")
    csv_header = next(csv_reader)
    file_to_output = "budget_analysis.txt"
    first_row = next(csv_reader)

    total_months += 1
    #total_months = total_months + 1
   
    total_profit_loss += int(first_row[1])
    #total_profit_loss = total_profit_loss + int(first_row[1])
  
    month_amount = int(first_row[1])
      
      
    for row in csv_reader:
        
        total_months = total_months + 1 
        monthly_change = int(row[1])-month_amount #
        total_profit_loss = total_profit_loss + int(row[1]) 
        profits.append(monthly_change) 
        month_amount = int(row[1])
        dates.append(row[0])  

        # net change = current month amount - past month amount
        # past month amount = int(row[1])
        # change list += net change
        # monthly average = sum(change list)/len(change list)
        
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

        
#os.getcwd

text_export = open(os.path.join("..","Pybank","Analysis", "Pybank.txt"), "w")

text_export.write("Financial Analysis\n")
text_export.write("------------------\n")
text_export.write(f"Total Months: {str(total_months)}\n")
text_export.write(f"Total: ${str(total_profit_loss)}\n")
text_export.write(f"Average Change: ${str(round(average,2))}\n")
text_export.write(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})\n")
text_export.write(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})\n")
text_export.close()


    


