import csv
import random
from names_generator import generate_name

# Giving random pupils from random teachers_subject_joins a random 

BenotungsAnzahl = 24569


def getFullNum(num):
	numS = str(num)
	if num < 10:
		return "0"+numS
	return numS


with open('faecher_lehrer_joined.csv',newline='') as faecher_lehrer_file:
	faecher_lehrer = csv.reader(faecher_lehrer_file, delimiter=';')
	faecher_lehrerListe = []
	for row in faecher_lehrer:
		faecher_lehrerListe.append(row) # get the primary keys

	with open('Schueler_randomDatabase.csv',newline='') as schuelerfile:
		schuelerr = csv.reader(schuelerfile, delimiter=';')
		schuelerListe = []
		for row in schuelerr:
			schuelerListe.append(row[0]) # get the primary key

		with open('Benotungen_randomDatabase.csv','w',newline='') as benotungfile:

			benotungen = csv.writer(benotungfile, delimiter=";")

			for row_num in range(BenotungsAnzahl):

				# use the number for ID
				schueler = random.randrange(0,len(schuelerListe))

				# use the number to get the primary key
				fach_lehrer = random.randrange(0,len(faecher_lehrerListe))

				date = str(random.randrange(2020,2022))+"-"+getFullNum(random.randrange(1,13))+"-"+getFullNum(random.randrange(1,29))

				note = random.randrange(1,7)

				benotungen.writerow([	schueler,
										faecher_lehrerListe[fach_lehrer][0],
										faecher_lehrerListe[fach_lehrer][1],
										note,
										date])




