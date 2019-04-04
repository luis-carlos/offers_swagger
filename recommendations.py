import json
import os
import sys

source_file = sys.argv[1]
customer = sys.argv[2]
channel = sys.argv[3]

metrics = {
    "cntRecommendations": "Recommendations",
    "cntAccepts":"Accepts",
    "cntClicks":"Clicks",
    "cntAddsToCart":"Adds"
}

csv_file = "data/" + customer + "/outcome/metrics-dedup.csv"
csv = open(csv_file, "a")

def parseJSON(csv, data, metricName, metricText, channel):
    totalMetric = 0
    for day in data['productTrends'][channel]['day1'][metricName]:
        totalMetric += day["v"]
        timestamp = str(day["n"])[5:7] + "/" + str(day["n"])[8:10] + "/" + str(day["n"])[:4] + str(day["n"])[10:]
        row = timestamp  + "," + metricText +  "," + str(day["v"]) + "," + timestamp + metricText + "\n"
        csv.write(row)
    print (str(totalMetric), metricText)
 
#open the file
with open(source_file) as f:
  data = json.load(f)

#File headers
if os.path.getsize(csv_file) == 0:
    csv.write("Timestamp,Metric,Count\n")
  
for x, y in metrics.items():
    parseJSON(csv, data, x, y, channel)

#Remove the source file
if os.path.isfile(source_file):
    os.remove(source_file)
    print("File was removed successfully")
else:
    print("Error removing " + str(source_file) + " file")

csv.close()

