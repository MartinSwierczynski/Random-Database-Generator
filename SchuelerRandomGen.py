import csv
import random
import datetime
from names_generator import generate_name

dataRows = 53297
genders = ["w","m"]

def getFullNum(num):
	numS = str(num)
	if num < 10:
		return "0"+numS
	return numS

minDate = datetime.datetime(1960,1,1)
maxDate = datetime.datetime(2005,12,31)

with open("Klassen.csv",newline="") as klassfile:
	# import all classes
	klassen = csv.reader(klassfile)
	klassenListe = []
	for row in klassen:
		klassenListe += row

	with open("Schueler_randomDatabase.csv","w", newline="") as csvfile:

		spamwriter = csv.writer(csvfile, delimiter=";")
		
		for row in range(dataRows):
			name = generate_name(style='capital')
			print(name)
			name = name.split()
			
			# random generate the time between your desired timestamps (min,max)
			randUnixTime = random.randrange(int(minDate.timestamp()),int(maxDate.timestamp()))
			
			# convert the unix time to a datetime
			date = datetime.datetime.fromtimestamp(randUnixTime)

			# convert the datetime to a American formated string
			dateStr = str(date.year)+"-"+getFullNum(date.month)+"-"+getFullNum(date.day)

			gender = genders[random.randrange(0,2)]

			currentClass = klassenListe[random.randrange(0,len(klassenListe))]

			spamwriter.writerow([name[1],name[0],dateStr,gender,currentClass])

