import csv
import operator

path = "Resources/election_data.csv"
with open(path) as csvfile:
	reader = csv.reader(csvfile)
	results = open("results.txt", 'w') 

	namearray  = {}
	votecounter = 0
	next(reader, None) #skip header row

	for row in reader:
		votecounter += 1
		name = row[1]
		if name not in namearray:
			namearray[name] = 1
		else:
			namearray[name] += 1
	print("Election Results \n --------------------")
	results.write("Election Results \n --------------------")
	print("Total Votes:" , votecounter, "\n --------------------")
	results.write("\nTotal Votes:" + str(votecounter) + "\n --------------------")
	for name, count in namearray.items():
		print(name, round((count / votecounter * 100), 3),"%" ,count)
		results.write('\n'+str(name)+ str(round((count / votecounter * 100), 3))+"%" +str(count))
	winner = max(namearray.items(), key = operator.itemgetter(1))[0]
	print( "----------------------\nAnd the Winner is.....", winner+"!")
	results.write("\n----------------------\nAnd the Winner is..... "+ winner+"!")
	results.close()



