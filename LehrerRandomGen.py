import csv
import random
from names_generator import generate_name

dataRows = 30
genders = ["w","m"]

# adds a zero if the number is below 10
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
	
	with open("Lehrer_randomDatabase.csv","w", newline="") as lehrerfile:

		lehrer = csv.writer(lehrerfile, delimiter=";")
		
		for row in range(dataRows):
			name = generate_name(style='capital')
			name = name.split()

			# assign all the classes till there are none
			if row < len(klassenListe):
				currentClass = klassenListe[row]
			else:
				currentClass = "NULL"

			lehrer.writerow([name[1],name[0],currentClass])

