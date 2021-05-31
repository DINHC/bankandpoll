import os 
import csv 

election = os.path.join("Resources", "election_data.csv")

candidates = []
vote_count = []
vote_percentage = []
vote_amount = 0 

    with open(election) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =",")
        csv_header = next(csv_reader)
        file_to_output = "election_data.txt"
   
        for row in csv_reader: 
            vote_amount += 1 

        
        for votes in vote_amount: 
            percent = (votes/vote_amount) * 100 
            percent = round(percent)
            percent = "{:.2%}".format(percent)
            vote_percentage.append(percent)

        