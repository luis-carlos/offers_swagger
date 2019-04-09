import glob
import json
import os
from csv import writer
from sys import argv
from datetime import date

customer = argv[1]
preferences_file = "preferences.json"

#Parse function
def parseJSON(data,limit):
    row = []
    for idx, product in enumerate(data['products'][:limit], start=1):
        row.append(str(date.today().strftime("%m/%d/%y")))
        row.append(str(idx))
        row.append(str(product['productId']))
        row.append(str(product['name']))
        row.append(str(product['productAnalytics']['day1']['recommendations']))
        row.append(str(product['productAnalytics']['day1']['clicks']))
        row.append(str(product['productAnalytics']['day1']['cart']))
        row.append(str(product['productAnalytics']['day1']['accepts']))
        csv_object.writerow(row)
        row = []
                
csv_file = "data/" + customer + "/outcome/top-products.csv"
csv_object = writer(open(csv_file, "a", newline=''))

#Looking for source file
files_path = "data\\" + customer + "\\*.json"
myList = [f for f in glob.glob(files_path)]
source_file = myList[0]

#open the file
with open(source_file) as f:
  data = json.load(f)

#File headers
if os.path.getsize(csv_file) == 0:
    csv_object.writerow(["Date","Position","Product ID", "Product Name", "Recommendations", "Clicks", "Adds to Cart", "Accepts"])

#Retrieve number of products from JSON file
with open(preferences_file) as f:
    limit = json.load(f)
limit = limit["preferences"]["top-products"]["daily-amount"]        

parseJSON(data, limit)

#Remove the source file
if os.path.isfile(source_file):
    os.remove(source_file)
    print("File was removed successfully")
else:
    print("Error removing " + str(source_file) + " file")


print("Successful file update")

