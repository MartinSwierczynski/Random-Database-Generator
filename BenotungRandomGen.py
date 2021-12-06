import csv
import random
from names_generator import generate_name

# Giving random pupils from random teachers_subject_joins a random grade

BenotungsAnzahl = 24569

minDate = datetime.datetime(2020,1,1)
maxDate = datetime.datetime.now()

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

				# random generate the time between your desired timestamps (min,max)
				randUnixTime = random.randrange(minDate.timestamp(),maxDate.timestamp())
				# convert the unix time to a datetime
				date = datetime.datetime.fromtimestamp(randUnixTime)
				# convert the datetime to a American formated string
				dateStr = str(date.year)+"-"+getFullNum(date.month)+"-"+getFullNum(date.day)


				note = random.randrange(1,7)

				benotungen.writerow([	schueler,
										faecher_lehrerListe[fach_lehrer][0],
										faecher_lehrerListe[fach_lehrer][1],
										note,
										dateStr])




