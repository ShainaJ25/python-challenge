# import the os module
import os

# Module for reading csv file
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')


#Create lists to store data
Total_months = []
Total_profit_losses = [] 
Change_profit_losses = []

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip header labels
    csv_header = next(csv_reader)

    #Read through each row of data after the header
    for row in csv_reader:

        #Add total months 
        Total_months.append(row[0])

        #Add total profit/losses
        Total_profit_losses.append(int(row[1]))

    #loop through profits/losses
    for x in range(len(Total_profit_losses)-1):

        #Find the change in profit/losses 
        Change_profit_losses.append(Total_profit_losses[x+1]-Total_profit_losses[x])

    #Find the Maximum and Minimum Date
    Maximum_profit = Change_profit_losses.index(max(Change_profit_losses)) + 1
    Minimum_profit = Change_profit_losses.index(min(Change_profit_losses)) + 1

    #Find the Maximum and Minimum Value
    Maximum_increase = max(Change_profit_losses)
    Minimum_decrease = min(Change_profit_losses)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Total_months)}")
print(f"Total: ${sum(Total_profit_losses)}")
print(f"Average Change: ${round(sum(Change_profit_losses)/len(Change_profit_losses),2)}")
print(f"Greatest Increase in Profits: {Total_months[Maximum_profit]} (${(str(Maximum_increase))})")
print(f"Greatest Decrease in Profits: {Total_months[Minimum_profit]} (${(str(Minimum_decrease))})")



# Specify the file to write to
output_file = os.path.join("Analysis", "budget_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w', newline='') as cvsfile:
    writer = csv.writer(cvsfile, delimiter=',')

     # Write the header and separator lines as lists
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------"])
   
   # Write total months
    writer.writerow([f"Total Months: {len(Total_months)}"])

   # Write total sum
    writer.writerow([f"Total: ${sum(Total_profit_losses)}"]) 
    
    # Write the average change
    writer.writerow([f"Average Change: ${round(sum(Change_profit_losses)/len(Change_profit_losses),2)}"])

    # Write the greatest increase
    writer.writerow([f"Greatest Increase in Profits: {Total_months[Maximum_profit]} (${(str(Maximum_increase))})"])

    # Write the greatest decrease
    writer.writerow([f"Greatest Decrease in Profits: {Total_months[Minimum_profit]} (${(str(Minimum_decrease))})"])







    

    











