import os 
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

total_votes = 0
khan = 0
correy = 0
li = 0
tooley = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next (csvfile)

    for row in csvreader: 
        total_votes = total_votes + 1 
    
        if (row[2] == "Khan"):
            khan = khan + 1

        elif(row[2] == "Correy"):
            correy = correy +1

        elif(row[2] == "Li"):
           li = li + 1

        else: 
          tooley = tooley + 1

khan_percent = khan / total_votes
correy_percent = correy / total_votes
li_percent =  li / total_votes
tooley_percent = tooley / total_votes

winner = max(khan, correy, li, tooley)

if winner == khan:
    winner_name = "Khan"
elif winner == correy:
    winner_name = "Correy"
elif winner == li:
    winner_name = "Li"
else:
    winner_name = "O'Tooley"

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {khan_percent:.3%}({khan})")
print(f"Correy: {correy_percent:.3%}({correy})")
print(f"Li: {li_percent:.3%}({li})")
print(f"O'Tooley: {tooley_percent:.3%}({tooley})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

with open("PyPoll.txt", 'w',) as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {khan_percent:.3%}({khan})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li})\n")
    txtfile.write(f"O'Tooley: {tooley_percent:.3%}({tooley})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")