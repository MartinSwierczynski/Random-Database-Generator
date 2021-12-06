import csv
import random
from names_generator import generate_name

# its joining each teacher into a subject. Eather 1 or <maxfaecher>

maxfaecher = 3+1

with open('Lehrer_randomDatabase.csv',newline='') as lehrerfile:
	lehrer = csv.reader(lehrerfile, delimiter=';')
	lehrerListe = []
	for row in lehrer:
		lehrerListe.append(row[1]) # get the primary key
	
	with open('Faecher.csv',newline='') as faecherfile:
		faecher = csv.reader(faecherfile, delimiter=';')
		faecherListe = []
		for row in faecher:
			faecherListe += row # get the primary key

		with open('faecher_lehrer_joined.csv','w',newline='') as faecher_lehrer_file:

			lehrer_facher = csv.writer(faecher_lehrer_file, delimiter=";")
			# for each lehrer
			for row_num in range(len(lehrerListe)):
				# which facher it has
				lehrer_faecher = []
				# how much facher it is allowed to have
				faecher_count = random.randrange(0,maxfaecher)
				
				# random give it faecher (without duplicates)
				for fach in range(faecher_count):
					# loop the current fach till it random generates one that isn't duplicated
					it_already_has_fach = True
					while (it_already_has_fach):
						# random generate a index number from the faecherListe to get a fach
						fach = random.randrange(0,len(faecherListe))
						
						try:
							lehrer_faecher.index(fach)
						except ValueError:
							it_already_has_fach = False
					lehrer_faecher.append(fach)
					# save the lehrer with its fach
					#print([lehrerListe[row_num],faecherListe[fach]])
					lehrer_facher.writerow([lehrerListe[row_num],faecherListe[fach]])

