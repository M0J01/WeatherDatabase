__author__ = 'Jo'

cities = 50
years = 55
days=365*years
datapoints=days*cities

smallplan = datapoints/500 + 1

print "The number of total data points will be %s" % (datapoints)

print "time till done with %s cities = %s with 500 pulls per day" % (cities, smallplan)
