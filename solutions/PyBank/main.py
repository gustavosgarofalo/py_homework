#insert the necessary modules
import os
import csv
import pandas as pd

#variable storage for month count and profit/loss sum
profloss_sum=0
month_count=0

#create variable path
csv_path=os.path.join('..','..','Instructions', 'PyBank', 'Resources', 'budget_data.csv')


#open and read through the file, using the path created
#creating a variable to store the csv file, each line as a list
with open(csv_path, newline='') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    

#taking out the column labels, separating each label in one row
    csv_labels=next(csv_reader)
     #print(f'csv_header{csv_labels}')
    date_lab=csv_labels[0]
    profloss_lab=csv_labels[1]

#loop through the each column using list comprehension
    for row in csv_reader:
        if row[0] is not None:
            month_count += 1
        if row is not None:
            profloss_sum += int(row[1])

#creating panda dataframe with the module    
df_file=pd.read_csv(csv_path)
#applying difference function to create a new Delta column
df_file['Delta']=df_file['Profit/Losses'].diff().shift(0)
delta_avr=df_file['Delta'].mean()
low_diff=df_file['Delta'].min()
high_diff=df_file['Delta'].max()

#Setting Delta column as index to look for the respective date of maximum decrease
df_new=df_file.set_index('Delta')
min_date=df_new.loc[low_diff, 'Date']
max_date=df_new.loc[high_diff, 'Date']


#printing all the solutions
# 
print('                               ') 
print("Financial Analysis")
print('-------------------------------')
print('Total Months: ', month_count)
print('Total: $', profloss_sum)
print("Average Change: ", round(delta_avr,2))
print('Greatest Increase in Profits: ', max_date, '($', int(high_diff), ')' )
print('Greatest Decrease in Profits: ', min_date, '($', int(low_diff), ')')
    

#writing the results in a new txt file
output_path=os.path.join('output.csv')

#assessing output file but for write mode now
with open(output_path, 'w', newline='') as output_file:
    output_writer=csv.writer(output_file)

    #create the first line for the headers
    output_writer.writerow(['                               '])
    output_writer.writerow(["Financial Analysis"])
    output_writer.writerow(['-------------------------------'])
    output_writer.writerow(['Total Months: ', month_count])
    output_writer.writerow(['Total: $', profloss_sum])
    output_writer.writerow(["Average Change: ", round(delta_avr,2)])
    output_writer.writerow(['Greatest Increase in Profits: ', max_date, '($', int(high_diff), ')' ])
    output_writer.writerow(['Greatest Decrease in Profits: ', min_date, '($', int(low_diff), ')'])
   
    