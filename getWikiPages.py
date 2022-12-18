from configparser import ConfigParser
import requests
import json
import os

#Read config.ini file
configObject = ConfigParser()
configObject.read("config.ini")

# Constants
FANDOM_HOST=configObject["GENERAL"]["host"]
CARGO_EXPORT_HOST=configObject["CARGOEXPORT"]["host"]
MAXIMUM_QUERY_COUNT=int(configObject["CARGOEXPORT"]["maxcount"])
JSON_OUTPUT_FILE=configObject["GENERAL"]["generateddict"] + "wiki-pages.json"

path = configObject["GENERAL"]["generateddict"]
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory " + path + " is created!")
   
# Send a GET request to Special:CargoExport to get Card table object with the most recent build
tableUrl = CARGO_EXPORT_HOST + "?tables=WikiTable&&fields=WikiTable._pageTitle%2C+WikiTable.build&where=WikiTable._pageTitle%3D%22Card2+table%22+OR+WikiTable._pageTitle%3D%22Card+table%22&order+by=%60cargo__WikiTable%60.%60build%60+DESC&limit=1&format=json"
tableObject = requests.get(url=tableUrl).json()
cardTableName = ""

print("Table object: " + str(tableObject[0]))

# Wiki has 2 different Card tables, Card and Card2, whose build are different. We only take one with the most recent build
if (tableObject[0]["_pageTitle"] == "Card table"):
	cardTableName = "Card"
else:
	cardTableName = "Card2"

# Send a GET request to Special:CargoExport to get Card objects
basePageUrl = CARGO_EXPORT_HOST + "?tables=" + cardTableName + "%2C+CustomCard&join+on=" + cardTableName + ".dbfId%3DCustomCard.dbfId&fields=CustomCard.dbfId%3DdbfId%2C+" + cardTableName + ".id%3Did%2C+CustomCard._pageName%3Dpage&where=CustomCard._pageName+IS+NOT+NULL&order+by=%60cargo__CustomCard%60.%60_pageName%60&limit=5000&format=json"

# Initialization
offset = 0 # Special:CargoExport is only able to return 5000 objects per query. This serves as the checkpoint and is increased by 5000 every query
cardCount = MAXIMUM_QUERY_COUNT # Initializing maximum card count
cardPages = [] # Array to store card objects from all queries

# Get multiple queries until the cardCount is lower than 5000 (which means there are no more cards needed)
print("Generating " + JSON_OUTPUT_FILE + "...")
while cardCount >= MAXIMUM_QUERY_COUNT:
	offsetUrl = basePageUrl + "&offset=" + str(offset) #Add param offset to the request
	cardJsonObject = requests.get(url=offsetUrl).json() # Send GET request, then turn the content into json object
	for card in cardJsonObject: # Format the page key so that it represents the link to Wiki article
		card["page"] = FANDOM_HOST + str(card["page"]).replace(" ", "_").replace("&quot;", "\"").replace("?", "%3F")
	cardPages.extend(cardJsonObject) # Add the result to the array
	cardCount = len(cardJsonObject)
	offset += MAXIMUM_QUERY_COUNT

with open(JSON_OUTPUT_FILE, 'w') as outfile:
	json.dump(cardPages, outfile, indent=1)
	
print("Generated " + JSON_OUTPUT_FILE + " successfully")
print("Total cards: " + str(len(cardPages)))