__author__ = 'Jo'

write_file = open('C:/Weather/WeatherPackage/WeatherDirectory/teststuff.txt', "w")

string = ['not really', 'a string here']

for line in string:
    write_file.write(line +',' + '\n')
