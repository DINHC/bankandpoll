import os 
import csv 

election = os.path.join("Resources", "election_data.csv")

candidates = []
vote_count = []
vote_percentage = []
vote_amount = 0 

with open(election) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")
        csv_header = next(csv_reader)
        file_to_output = "election_data.txt"
   
        for row in csv_reader:  
            vote_amount += 1 
        
            if row[2] not in candidates:
                candidates.append(row[2])
                index = candidates.index(row[2])
                vote_count.append(1)
            else:
                index = candidates.index(row[2])
                vote_count[index] += 1
        
for votes in vote_count: 
    percent = (votes/vote_amount) * 100 
    percent = round(percent)
    percent = "%.3f%%" % percent
    vote_percentage.append(percent)

winner = max(vote_count)
index = vote_count.index(winner)
win_candidate = candidates[index]

print("Election Results")
print("----------------------")
print(f"Total Votes: {str(vote_amount)}")
print("----------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(vote_percentage[i])} ({str(vote_count[i])})")
print("--------------------------")
print(f"Winner: {win_candidate}")
print("--------------------------")


text_export = open(os.path.join("..","Pypoll","Analysis", "Pypoll.txt"), "w")

text_export.write("Election Results\n")
text_export.write("------------------\n")
text_export.write(f"Total Votes: {str(vote_amount)}\n")
text_export.write("------------------\n")
for i in range(len(candidates)):
    text_export.write(f"{candidates[i]}: {str(vote_percentage[i])} ({str(vote_count[i])})\n")
text_export.write("--------------------\n")
text_export.write(f"Winner: {win_candidate}\n")
text_export.write("--------------------\n")
text_export.close()
