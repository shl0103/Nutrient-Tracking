import urllib, json


url = 'http://api.nal.usda.gov/ndb/reports/'

#data =  {'api_key': 'CaYB3CPpVop4oXocZ79CRO5LqKw9YoMs4OkRwUmN', 'ndbno': '01009', 'type':'b', 'format': 'xml'}
#params = urllib.urlencode(data)
#print params

url= url + "?" + "ndbno=01009" + "&" + "type=b" + "&" + "format=json" +"&" +"api_key=CaYB3CPpVop4oXocZ79CRO5LqKw9YoMs4OkRwUmN" 
print url
response = urllib.urlopen(url)
data = json.load(response)
print data
