import sys
import glob
import json

customer = sys.argv[1]

#Parse function
def parseJSON(data):
    x = 0
    for product in data['products']:
        if (x<25):
            print("-"*50)
            print(product['name'] + " (" + product['productId'] + ")")
            print("Recommendations: " + str(product['productAnalytics']['day1']['recommendations']))
            print("Clicks: " + str(product['productAnalytics']['day1']['clicks']))
            print("Adds to cart: " + str(product['productAnalytics']['day1']['cart']))
            print("Accepts: " + str(product['productAnalytics']['day1']['accepts']))
        x += 1
        



#Looking for source file
files_path = "data\\" + customer + "\\*.json"
myList = [f for f in glob.glob(files_path)]
source_file = myList[0]

#open the file
with open(source_file) as f:
  data = json.load(f)

parseJSON(data)

