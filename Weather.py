__author__ = 'Jo'

#Key ID


import urllib2
import json

address = 'http://api.wunderground.com/api/Your_Key/geolookup/conditions/q/IA/Cedar_Rapids.json'

file = urllib2.urlopen(address)
json_string = file.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current Temperature in %s is: %s" % (location, temp_f)
file.close()