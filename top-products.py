import sys
import glob
import json
import os
from datetime import date

customer = sys.argv[1]
preferences_file = "preferences.json"

#Parse function
def parseJSON(data,limit):
    x = 0
    for product in data['products']:
        if (x<limit):
            print("-"*50)
            print("Date: " + date.today().strftime("%m/%d/%y"))
            print("Position: " + str(x+1))
            print(product['name'] + " (" + product['productId'] + ")")
            print("Recommendations: " + str(product['productAnalytics']['day1']['recommendations']))
            print("Clicks: " + str(product['productAnalytics']['day1']['clicks']))
            print("Adds to cart: " + str(product['productAnalytics']['day1']['cart']))
            print("Accepts: " + str(product['productAnalytics']['day1']['accepts']))
        x += 1
        
csv_file = "data/" + customer + "/outcome/top-products.csv"
csv = open(csv_file, "a")

#Looking for source file
files_path = "data\\" + customer + "\\*.json"
myList = [f for f in glob.glob(files_path)]
source_file = myList[0]

#open the file
with open(source_file) as f:
  data = json.load(f)

#File headers
if os.path.getsize(csv_file) == 0:
    csv.write("Date,Position,Product ID, Product Name, Recommendations, Clicks, Adds to Cart, Accepts\n")

#Retrieve number of products from JSON file
with open(preferences_file) as f:
    limit = json.load(f)
limit = limit["preferences"]["top-products"]["daily-amount"]        

parseJSON(data, limit)

csv.close()

