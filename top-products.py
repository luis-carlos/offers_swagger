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
    row = ""
    for product in data['products']:
        if (x<limit):
            row += str(date.today().strftime("%m/%d/%y") + ",") 
            #print("Date: " + date.today().strftime("%m/%d/%y"))
            row += str(x+1) + ","
            #print("Position: " + str(x+1))
            row += str(product['productId']) + ","
            #print(product['name'] + " (" + product['productId'] + ")")
            row += str(product['name']) + ","
            #print("Recommendations: " + str(product['productAnalytics']['day1']['recommendations']))
            row += str(product['productAnalytics']['day1']['recommendations']) + ","
            #print("Clicks: " + str(product['productAnalytics']['day1']['clicks']))
            row += str(product['productAnalytics']['day1']['clicks']) + ","
            #print("Adds to cart: " + str(product['productAnalytics']['day1']['cart']))
            row += str(product['productAnalytics']['day1']['cart']) + ","
            #print("Accepts: " + str(product['productAnalytics']['day1']['accepts']))
            row += str(product['productAnalytics']['day1']['accepts']) + "\n"
            #print(row)
            csv.write(row)
            row=""
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

print("Successful file update")

