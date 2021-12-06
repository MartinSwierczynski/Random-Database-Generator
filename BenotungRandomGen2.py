import csv
import random
import datetime
from names_generator import generate_name

# Giving all pupils from random teachers_subject_joins 2 to 20 random grades 

minNoten = 2
maxNoten = 20

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
			schuelerListe.append(row[0]) # get the name... the list adds up the names and syncs with the auto increment of mysql for the primary key

		with open('Benotungen_randomDatabase.csv','w',newline='') as benotungfile:

			benotungen = csv.writer(benotungfile, delimiter=";")

			for schuelerID in range(len(schuelerListe)):
				dates = []
				for noten in range(0,random.randrange(minNoten,maxNoten)):

					# use the number to get the primary key
					fach_lehrer = random.randrange(0,len(faecher_lehrerListe))

					dateStr = ""

					# loop the current fach till it random generates one that isn't duplicated
					it_already_has_date = True
					while (it_already_has_date):
						# random generate the time between your desired timestamps (min,max)
						randUnixTime = random.randrange(int(minDate.timestamp()),int(maxDate.timestamp()))
						# convert the unix time to a datetime
						date = datetime.datetime.fromtimestamp(randUnixTime)
						# convert the datetime to a American formated string
						dateStr = str(date.year)+"-"+getFullNum(date.month)+"-"+getFullNum(date.day)

						
						try: # if it can find it then repeat
							dates.index(dateStr)
						except ValueError: # if it errors to find it then make it False and continue
							it_already_has_date = False

					note = random.randrange(1,7)

					benotungen.writerow([	schuelerID,
											faecher_lehrerListe[fach_lehrer][0],
											faecher_lehrerListe[fach_lehrer][1],
											note,
											dateStr])




