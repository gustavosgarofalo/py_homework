#importing necessary modules
import os
import csv

#count variables
vote_count=0
khan_count=0
correy_count=0
li_count=0
tooley_count=0


#Empty lists
winner=[]

#setting up the path for file into a variable
csv_path=os.path.join('..', '..', 'datasets', 'PyPoll', 'Resources', 'election_data.csv')

#Opening and reading file, storing in pypoll variable
with open(csv_path, newline='') as csv_file:
    pypoll=csv.reader(csv_file, delimiter=',')

#Taking out headers of the database
    pypoll_labels=next(pypoll)

#Loop trough voter id column to count and to store percentsge of votes
    
    for row in pypoll:
        if row[0] is not None:
            vote_count += 1

        if row[2] == "Khan":
            khan_count += 1
            k_percent=round((khan_count/vote_count)*100)

        if row[2] == "Correy":
            correy_count += 1
            c_percent= round((correy_count/vote_count)*100)

        if row[2] == "Li":
            li_count += 1
            l_percent=round((li_count/vote_count)*100)

        if row[2] == "O'Tooley":
            tooley_count +=1
            t_percent=round((tooley_count/vote_count)*100)

#Conditionals statement to exhibit the winner by comparing the percentages of votes

    if (c_percent<k_percent) and (l_percent < k_percent) and (t_percent < k_percent):
        w="Khan"
        winner.append(w)
    
    if (c_percent<t_percent) and (l_percent < t_percent) and (k_percent < t_percent):
        w="O`Tooley"
        winner.append(w)
    
    if (c_percent<l_percent) and (k_percent < l_percent) and (t_percent < l_percent):
        w="Li"
        winner.append(w)

    if (k_percent<c_percent) and (l_percent < c_percent) and (t_percent < c_percent):
        w="Correy"
        winner.append(w)
    

#Printing all of the results
print('Election Results')
print('-----------------------------------')
print('Total Votes: ', vote_count)
print('-----------------------------------')
print("Khan: ", k_percent, '%', '(', khan_count, ')')
print("Correy: ", c_percent, '%', '(', correy_count, ')')
print("Li: ", l_percent, '%', '(', li_count, ')')
print("O'Tooley: ", t_percent, '%', '(', tooley_count, ')')
print('-----------------------------------')
print("Winner :", winner)
print('-----------------------------------')


output_path='output.csv'
with open(output_path, 'w', newline='') as output_file:
    output_writer=csv.writer(output_file)

    #create the first line for the headers
    output_writer.writerow(['Election Results'])
    output_writer.writerow(['-----------------------------------'])
    output_writer.writerow(['Total Votes: ', vote_count])
    output_writer.writerow(['-----------------------------------'])
    output_writer.writerow(["Khan: ", k_percent, '%', '(', khan_count, ')'])
    output_writer.writerow(["Correy: ", c_percent, '%', '(', correy_count, ')'])
    output_writer.writerow(["Li: ", l_percent, '%', '(', li_count, ')' ])
    output_writer.writerow(["O'Tooley: ", t_percent, '%', '(', tooley_count, ')'])
    output_writer.writerow(['-----------------------------------'])
    output_writer.writerow(["Winner :", winner])
    output_writer.writerow(['-----------------------------------'])