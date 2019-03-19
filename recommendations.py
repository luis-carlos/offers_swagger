import json
import os
import sys

totalRecommendations = 0
totalAccepts = 0
totalClicks = 0
totalAddsToCart = 0

csv_file = "data/outcome/metrics-dedup.csv"
csv = open(csv_file, "a")
 
#open the file
with open(sys.argv[1]) as f:
  data = json.load(f)

#File headers
if os.path.getsize(csv_file) == 0:
    csv.write("Timestamp,Metric,Count\n")
  
#Read all recommendations
for day in data['productTrends']['ecom']['day1']['cntRecommendations']:
    totalRecommendations += day["v"]
    timestamp = str(day["n"])[5:7] + "/" + str(day["n"])[8:10] + "/" + str(day["n"])[:4] + str(day["n"])[10:]
    metric = "Recommendations"
    row = timestamp  + "," + metric +  "," + str(day["v"]) + "," + timestamp + metric + "\n"
    csv.write(row)
print (str(totalRecommendations) + " recommendations")  

#Read all accepts  
for day in data['productTrends']['ecom']['day1']['cntAccepts']:
    totalAccepts += day["v"]
    timestamp = str(day["n"])[5:7] + "/" + str(day["n"])[8:10] + "/" + str(day["n"])[:4] + str(day["n"])[10:]
    metric = "Accepts"
    row = timestamp  + "," + metric + "," + str(day["v"]) + "," + timestamp + metric + "\n"
    csv.write(row)
print (str(totalAccepts) + " accepts")

#Read all clicks  
for day in data['productTrends']['ecom']['day1']['cntClicks']:
    totalClicks += day["v"]
    timestamp = str(day["n"])[5:7] + "/" + str(day["n"])[8:10] + "/" + str(day["n"])[:4] + str(day["n"])[10:]
    metric = "Clicks"
    row =  timestamp + "," + metric + "," + str(day["v"]) + "," + timestamp + metric + "\n"
    csv.write(row)
print (str(totalClicks) + " clicks")

#Read all clicks  
for day in data['productTrends']['ecom']['day1']['cntAddsToCart']:
    totalAddsToCart += day["v"]
    timestamp = str(day["n"])[5:7] + "/" + str(day["n"])[8:10] + "/" + str(day["n"])[:4] + str(day["n"])[10:]
    metric = "Adds"
    row =  timestamp + "," + metric + "," + str(day["v"]) + "," + timestamp + metric + "\n"
    csv.write(row)
print (str(totalAddsToCart) + " Adds to cart")

 
#reading file
csv.close()

