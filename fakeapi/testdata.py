#!/usr/bin/env python3

import os
import random
from datetime import date


weekdays=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
months= {'Jan':'01','Feb':'02','Mar':'03',
 		 'Apr':'04','May':'05','Jun':'06',
 		 'Jul':'07','Aug':'08','Sep':'09',
 		 'Oct':'10','Nov':'11','Dec':'12'}
# Keys die Monatskürzel
# Values sind die Monatsnummern

days= {'Jan':'31','Feb':'28','Mar':'31',
 	   'Apr':'30','May':'31','Jun':'30',
 	   'Jul':'31','Aug':'31','Sep':'30',
 	   'Oct':'31','Nov':'30','Dec':'31'}

# Keys sind die Anzahl der Tage
# Values die Monatskürzel


# counts_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10',
#            '11','12','13','14','15','16','17','18','19','20',
#            '21','22','23','24','25','26','27','28','29','30',
#            '31']
# counts_2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10',
#            '11','12','13','14','15','16','17','18','19','20',
#            '21','22','23','24','25','26','27','28','29','30']
# counts_3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10',
#            '11','12','13','14','15','16','17','18','19','20',
#            '21','22','23','24','25','26','27','28']

# monat = 'May'

def date_randomizer(monat):
	# date(2017, 5, 13)	
	# Syntax: date(jahr, monat, tag)
	laufvar_1=1
	laufvar_2=1
	wdays = []
	year = 2017


	if monat in months.keys():
		while laufvar_1 < (int(days[monat])+1):
			today = date(year, int(months[monat]), laufvar_1).weekday()
			# gibt eine zahl aus, die mit weekdays abgeglichen, den Tag ergibt
			wday = weekdays[today]
			wdays.append(wday)
			laufvar_1+=1

		return wdays

# Links: 
# datetime docs = https://docs.python.org/3/library/datetime.html
# time docs = https://docs.python.org/3/library/time.html#time.time
# random docs = https://docs.python.org/3.6/library/random.html?highlight=random#module-random

def time_randomizer():
	
	hour = 0
	minute = 0
	second = 0

	hour = int(round(random.random(),2)*100)
	minute = int(round(random.random(),2)*100)
	second = int(round(random.random(),2)*100)

	while hour > 23 :
		hour = int(round(random.random(),2)*100)

	if hour < 10:
		hour = '0'+str(hour)

	while minute > 59:
		minute = int(round(random.random(),2)*100)

	if minute < 10:
		minute = '0'+str(minute)

	while second > 59:
		second = int(round(random.random(),2)*100)

	if second < 10:
		second = '0'+str(second)

	return (hour,minute,second)


def produce(year,monat,wdays,hour,minute,second):
	
	x = 1
	y = 0
	
	# validator für .json-Dateien 	https://jsonlint.com/
	while x < 31:
		dataname = "mail"+str(x)+".json"
		path = '''<gewünschter Dateipfad>'''+dataname
		if os.path.exists(path):
			x+=1
		else:
			#print('ich bin hier reingegangen :)')
			while y < len(wdays):
				wday_set=wdays[y]
				print(wday_set)
				y +=1
				break

			with open(dataname,'w') as f:
				f.write('''
{
	"id": "203984091908",
	"internalDate": "'''+wday_set+' '+monat+' '+ str(x) +' '+str(hour)+':'+str(minute)+':'+str(second)+' '+str(year)+'''",
	"payload": {
		"mimeType": "text/html",
		"headers": [{
			"from": "sherlock@example.com",
			"to": "drwatson@example.com",
			"subject": " "

		}],
		"body": "This is an email"
	}
}
					''')
				f.close()
				print("erstellt")
			new_random = time_randomizer()
			hour = new_random[0]
			minute = new_random[1]
			second = new_random[2]
			x+=1


def main_method():
	monat= 'Apr'
	year = 2017
	step1 = date_randomizer(monat)
	print('Ok: ', step1)
	step2 = time_randomizer()
	print('ok: ', step2)
	produce(year,monat,step1,step2[0],step2[1],step2[2])
	print('all done')

main_method()
