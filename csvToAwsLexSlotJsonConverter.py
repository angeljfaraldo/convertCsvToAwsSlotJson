### to execute this python script the CLI command must be formatted as follows:
### python nameOfThisScript.py csvFileNameToBeConverted.csv(&fileLocation if necessary) titleOfSlot titleOfOutputJsonFile
### EXAMPLE:
### $ python csvToAwsLexSlotJsonConverter.py csvToConvert.csv newSlotName outputConvertedJsonFile.json

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
    "name": sys.argv[2],
    "version": "1",
    "enumerationValues": [],
   "valueSelectionStrategy": "TOP_RESOLUTION"
  }  
} 

with open(sys.argv[1]) as csvfile:
     reader = csv.reader(csvfile)
     csv_data =  ([{"value": row[0], "synonyms": (row)} for row in reader])
     csvfile.close()

with open(sys.argv[3], 'w') as jsonfile:
     jsonfile.write(json.dumps(data, indent=1))
     jsonfile.close()
     
with open(sys.argv[3], 'r+') as jsonf:
    data_2 = json.load(jsonf)
    data_2['resource']['enumerationValues'] = csv_data
    jsonf.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data_2, jsonf, indent=1)
    jsonfile.close()

# show result
with open(sys.argv[3], 'r') as jsonfile:
    print(json.dumps(json.load(jsonfile), indent=1))