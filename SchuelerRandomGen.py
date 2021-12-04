import csv
import random
from names_generator import generate_name

dataRows = 53297
genders = ["w","m"]

def getFullNum(num):
	numS = str(num)
	if num < 10:
		return "0"+numS
	return numS


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
			
			date = str(random.randrange(1960,2005))+"-"+getFullNum(random.randrange(1,13))+"-"+getFullNum(random.randrange(1,29))

			gender = genders[random.randrange(0,2)]

			currentClass = klassenListe[random.randrange(0,len(klassenListe))]

			spamwriter.writerow([name[1],name[0],date,gender,currentClass])

