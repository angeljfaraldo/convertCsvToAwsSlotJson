Convert Csv files into appropriate and formatted JSON for AWS's Lex Bot
prerequisites: 
  The .csv file must follow the format of 1st column "values" and "synonyms" to be placed in proceeding columns.  
  EX: 
    Column1:    Column2:      column3...
    "values"    "synonym"    "synonym"
### to execute this python script the CLI command must be formatted as follows:
### python nameOfThisScript.py csvFileNameToBeConverted.csv(&fileLocation if necessary) titleOfSlot titleOfOutputJsonFile
### EXAMPLE:
### $ python csvToAwsLexSlotJsonConverter.py csvToConvert.csv newSlotName outputConvertedJsonFile.json

