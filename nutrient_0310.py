import urllib, json, csv
import xml.etree.ElementTree as ET

url = 'http://api.nal.usda.gov/ndb/reports/?'
#def get_nutrition_data(ndbno, type, format, api_key):
json_data = []
data = None
write_header = True
item_keys = []



f_dump_file = "dump_tree"

f_dump = open(f_dump_file, 'w')

def recursion_xml(root, nutrient_group, nutrient):
    #root = tree.getroot()
    f_dump.write("\n")
    f_dump.write(str(root.tag))
    f_dump.write("\n")
    f_dump.write(str(root.attrib))
    if (root.tag == 'nutrient'):
        #print root.attrib
        if (root.attrib['group'] == nutrient_group and root.attrib['name'] == nutrient):
            print "value"
            print root.attrib['value']
            return root.attrib['value']
            #print root[0][0]
            
        
    for child in root:
        recursion_xml(child, nutrient_group, nutrient)
  
        
class Nutrition:

    def __init__(self,base_url):
        self.url = base_url

    def get_nutrition(self, ndbno, type_read, format_read, api_key):
        self.ndbno = ndbno
        self.type_read = type_read
        self.format_read = format_read
        self.api_key = api_key
        param = {'ndbno' : self.ndbno, 'type' : self.type_read, 'format': self.format_read, 'api_key' : self.api_key}
        param = urllib.urlencode(param)
        #print param
        response  = urllib.urlopen(self.url+param)
        data = response.read()
        #data = json.load(response)
        
        return data
    def get_nutrient(self, file1,nutrient_group, nutrient):#per 100
        tree = ET.parse(file1)
        root = tree.getroot()
        recursion_xml(root, nutrient_group, nutrient)
        f_dump.close()
        
        
nutrition = Nutrition(url)
data  = nutrition.get_nutrition('01009', 'b', 'xml', 'CaYB3CPpVop4oXocZ79CRO5LqKw9YoMs4OkRwUmN')
file1 = "/Users/aiswaryabhavanishankar/Documents/dump_xml.xml"

f1 = open(file1, 'w')
f1.write(str(data))
f1.close()
#f = csv.writer(open('file.csv', 'wb+'))

nutrition.get_nutrient(file1, 'Vitamins', 'Vitamin A, IU')
#tree = ET.parse(data)
#root = tree.getroot()

'''print root.tag
print root.attrib

