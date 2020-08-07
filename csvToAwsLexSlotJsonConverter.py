### to execute this python script the CLI command must be formatted as follows
### python csvFileNameToBeConverted(&location if necessary) TitleOfFile titleOfSlot 
### EXAMPLE:
### $ python botCsv2JsonConverter.py test.csv outputTesting.json newSlotName

import csv
import json
import sys



data = {
  "metadata": {
    "schemaVersion": "1.0",
    "importType": "LEX",
    "importFormat": "JSON"
  },
  "resource": {
    "name": sys.argv[3],
    "version": "1",
    "enumerationValues": [],
   "valueSelectionStrategy": "TOP_RESOLUTION"
  }  
} 

with open(sys.argv[1]) as csvfile:
     reader = csv.reader(csvfile)
     csv_data =  ([{"value": row[0], "synonyms": (row)} for row in reader])


with open(sys.argv[2], 'w') as jsonfile:
     jsonfile.write(json.dumps(data, indent=1))
     jsonfile.close()
     
with open(sys.argv[2], 'r+') as jsonfiles:
    data_2 = json.load(jsonfiles)
    data_2['resource']['enumerationValues'] = csv_data
    jsonfiles.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data_2, jsonfiles, indent=1)

# show result
with open(sys.argv[2], 'r') as jsonfile:
    print(json.dumps(json.load(jsonfile), indent=1))