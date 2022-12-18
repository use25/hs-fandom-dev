# hs-fandom-dev
This repository contains tools written in Python 3.6.0 to get data from Hearthstone Fandom for developers. In theory, you can just send GET requests to [CargoExport](https://hearthstone.fandom.com/wiki/Special:CargoExport) to retrieve the data in json format. However, the API still has flaws, such as generating uncleaned data with potentially special characters, incorrect data type; or unable to retrieve more than 5000 objects in a request.

Generally, these tools will:
* send GET requests to [CargoExport](https://hearthstone.fandom.com/wiki/Special:CargoExport) to retrieve the Hearthstone Wiki's data
* clean the data
* write the data in a generated JSON

## Setting up
* Your computer needs to download the Python environment to work. If it doesn't have yet, you can download from the official website [here](https://www.python.org/downloads/).
* After you set up the Python environment successfully, run command ``pip install -r requirements.txt`` to install required Python packages.

## Tools
You can use these tools by simply running the Python files (by command lines or whatever applications that supports Python). Most of these tools won't require any agruments, but rather have **Constants** declared at the top and served as configurations.
### getWikiPages
This tool will generate a JSON file containing **list of Card articles on Hearthstone Wiki**. Keys included:
* ``dbfId``: Official number id of the card.
* ``id``: Official string id of the card.
* ``page``: Full URL to the Hearthstone Wiki article describing the card.
Example:
```
[
 {
  "dbfId": 75742,
  "id": "PVPDR_GUEST_Diablot6",
  "page": "https://hearthstone.fandom.com/wiki/%3F%3F%3F_(75742)"
 }
]
```
*More tools will be coming soon as soon as I have sparing time to work on this repository.*

## Licensing
This repository is licensed under the terms of the MIT license.

## Community
* We have a [Discord channel](https://discord.gg/pJCYXfuaDs) where you can report or send feedback to me about anything related to Hearthstone Wiki, including articles or the developer tools. I may also be available in other media platforms, but usually Discord is where I'm most active.