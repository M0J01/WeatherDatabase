__author__ = 'Jo'

#Key ID

#address = 'http://www.wunderground.com/history/airport/KSAN/1960/10/1/MonthlyHistory.html?format=1'

#WARNING all public displays of information used from Wunderground must display Wunderground logo


#Updates
#Need to generate a list of awesome airports
#Need to store the information in a Text database for non-online retrieval
#Need to open a new text file for every new airport

import urllib2
import json

Airport_Names = [ 'Ronald Reagan Washingtion National',
                  'Johnson Field Onancock VA',
                  'Easton Newnam Field Airport VA',
                  'New London Forest Virginia',
                  'Bush Airport WoolWine VA',
                  'Twin County Galax Hillsville VA',
                  'Grundy Municipal Airport VA',
                  'Lee County Jonesville VA',
                  'Cottonwood Farm Crozet VA',
                  'Stokes Airport Goochland VA',
                  'Orange County Airport Orange VA',
                  'Fox Acres Airport Warrenton VA'




                 ]

airport_list = [ 'KDCA',
                 'VA91',
                 'KESN',
                 'KW90',
                 '6AV9',
                 'KHLX',
                 'KGDY',
                 'K0VG',
                 '87VA',
                 'VA15',
                 'KOHM',
                 '15VA'






                ]




add_base = 'http://www.wunderground.com/history/airport/'
add_end = '/1/MonthlyHistory.html?format=1'

add_year = 1947                     #Starting Year
add_month = 1                      #Starting Month
num_of_airports_searched = 0


for airport in airport_list:
    write_file = open('C:/Weather/WeatherPackage/WeatherDirectory/'+airport+'-' + Airport_Names[num_of_airports_searched] + '.txt', "w")
    Temperature_DataBase = ['PST','Max TemperatureF','Mean TemperatureF','Min TemperatureF',airport]

    while add_year < 2016:
        while add_month < 13:

            address = add_base + airport +'/' + str(add_year) +'/' + str(add_month) + add_end   #Construct the address to visit

            file = urllib2.urlopen(address)     #Open the Website Address
            text = str(file.read())             #Read Website Address as String
            lext =  text.split('\n')            #Split string by new lines (Line Text)

            for line in lext[2:-1]:
                Temperature_DataBase.append(line.split(',')[0:4])

            print add_year,'/', add_month
            file.close()
            add_month += 1
        add_month = 1
        add_year+=1

    for lines in Temperature_DataBase:
        for line in lines:
            write_file.write(line + ',')
        write_file.write('\n')

    add_year = 1948
    num_of_airports_searched+=1
    print 'Done!'
print 'Really Done'

