__author__ = 'Jo'

#Key ID - 49e2d83580af7e90
#Second Key  - 141d6f02b9e1e1de -(Emergency or testing purposes)

# Logo Website - http://www.wunderground.com/weather/api/d/docs?d=resources/logo-usage-guide
#WARNING - Must use logo in order to publicize/use findings

import urllib2
import json

address = 'http://api.wunderground.com/api/49e2d83580af7e90/history_19900227/geolookup/conditions/q/VA/Henrico.json'



file = urllib2.urlopen(address)
json_string = file.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
#date = parsed_json['date']
#mintempi = parsed_json['dailysummary']['mintempi']
#maxtempi = parsed_json['maxtempi']
#meantempi = parsed_json['meantempi']
#temp_f = parsed_json['current_observation']['temp_f']
#print "The Temperature in %s was: %s, and : %s, with an average of %s" % (location, mintempi, maxtempi, meantempi)
#print "The Min Temp Was %s" % (location)

print parsed_json['history']
print parsed_json['history']['utcdate']
print parsed_json['history']['dailysummary']
average = parsed_json['history']['dailysummary'][0]['meantempi']
max = parsed_json['history']['dailysummary'][0]['maxtempi']
min = parsed_json['history']['dailysummary'][0]['mintempi']
print "At the Henrico's Dr. Hospital, in %s..." % (location)
print "The average temperature was : %s, with a high of : %s, and a low of : %s" %(average, max, min)
#['observations'][0]['tempi']


file.close()