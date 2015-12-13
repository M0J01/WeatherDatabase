__author__ = 'Jo'

#Key ID

#address = 'http://www.wunderground.com/history/airport/KSAN/1960/10/1/MonthlyHistory.html?format=1'

#WARNING all public displays of information used from Wunderground must display Wunderground logo

import urllib2
import json


Temperature_DataBase = ['PST','Max TemperatureF','Mean TemperatureF','Min TemperatureF']

add_base = 'http://www.wunderground.com/history/airport/'
add_end = '/1/MonthlyHistory.html?format=1'
add_airport = 'KSAN'
add_year = 1947                     #Starting Year
add_month = 0                      #Starting Month


while add_year < 2016:

    while add_month < 13:

        address = add_base + add_airport +'/' + str(add_year) +'/' + str(add_month) + add_end   #Construct the address to visit

        file = urllib2.urlopen(address)     #Open the Website Address
        text = str(file.read())             #Read Website Address as String
        lext =  text.split('\n')            #Split string by new lines (Line Text)

        for line in lext[0:-1]:
            Temperature_DataBase.append(line.split(',')[0:4])

        print add_year,'/', add_month
        file.close()
        add_month += 1

    add_month = 1
    add_year+=1

add_year = 1948

for line in Temperature_DataBase:
    print line
print 'Done!'