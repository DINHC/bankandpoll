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
            