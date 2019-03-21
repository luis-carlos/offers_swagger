import json
import os
import sys

metrics = {
    "cntRecommendations": "Recommendations",
    "cntAccepts":"Accepts",
    "cntClicks":"Clicks",
    "cntAddsToCart":"Adds"
}

csv_file = "data/outcome/metrics-dedup.csv"
csv = open(csv_file, "a")

def parseJSON(csv, data, metricName, metricText):
    totalMetric = 0
    for day in data['productTrends']['ecom']['day1'][metricName]:
        totalMetric += day["v"]
        timestamp = str(day["n"])[5:7] + "/" + str(day["n"])[8:10] + "/" + str(day["n"])[:4] + str(day["n"])[10:]
        row = timestamp  + "," + metricText +  "," + str(day["v"]) + "," + timestamp + metricText + "\n"
        csv.write(row)
    print (str(totalMetric), metricText)
 
#open the file
with open(sys.argv[1]) as f:
  data = json.load(f)

#File headers
if os.path.getsize(csv_file) == 0:
    csv.write("Timestamp,Metric,Count\n")
  
for x, y in metrics.items():
    parseJSON(csv, data, x, y)

##parseJSON(csv, data, "cntRecommendations", "Recommendations")
##parseJSON(csv, data, "cntAccepts", "Accepts")
##parseJSON(csv, data, "cntClicks", "Clicks")
##parseJSON(csv, data, "cntAddsToCart", "Adds")

csv.close()

