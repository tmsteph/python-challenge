
import csv
from csv import reader


path = "Resources/budget_data.csv"

with open(path,newline="") as csvfile:
	reader = csv.reader(csvfile,delimiter=",",quotechar='|')


	month_count = 0
	total = 0
	preprofit = 0
	changecounter = 0
	next(reader, None)
	greatestincrease = 0
	greatestdecrease = 0
	for row in reader:
		#print(row)
		month_count += 1
		#print(row[1])
		profit = int(row[1])
		total += profit
		#print ("profit",profit)
		#print ("preprofit", preprofit)
		daily_change = profit - preprofit
		#print ("change" ,daily_change)
		changecounter += daily_change
		#print ("Changecounter" ,changecounter)
		preprofit = profit
		if profit > greatestincrease:
			greatestincrease = profit
		elif profit < greatestdecrease:
			greatestdecrease = profit
	average_change = changecounter / month_count
	print('\n\n',"Financial Analysis", "\n", "------------------------")
	print("Total months:", month_count)
	print("Total Profit/Loss:",profit)
	print("Average Change:", round(average_change))
	print("Greatest Increase", greatestincrease)
	print("Greatest Decrease", greatestdecrease )

	results = open("results.txt",'w')

	results.write("Financial Analysis"+ "\n-------------------------")
	results.write("\nTotal months:"+ str(month_count))
	results.write("\nTotal Profit/Loss:"+ str(profit))
	results.write("\nAverage Change:"+ str(round(average_change)))
	results.write("\nGreatest Increase "+ str(greatestincrease))
	results.write("\nGreatest Decrease "+ str(greatestdecrease))
