# WikiCardPool
Pools of cards for generation
|Key|Data Type|Description
|----| ----|----
|id|Integer|Wiki identifier, served as primary key
|mockupName|String|Wiki's internal string to describe the usage of the pool
|sectionName|String|Official pool name, displayed on Wiki articles
|description|Wikistring|Pool description, displayed on Wiki articles
|generatorDbfIds|Array of Integer|List of dbfIds of cards that use this pool to do something (usually generate cards)
|gameMode|Integer|0: Invalid, 1: Constructed / Traditional, 2: Arena, 3: Battlegrounds, 4: Duels, 5: Mercenaries
|ignoresFilters|Integer|1 if this pool only uses additionalPoolDbfIds and option keys (anything after isForGenerating), 0 otherwise
|costMore|Integer|Filters cards that cost VALUE or more. -1 if it has no such condition
|costLess|Integer|Filters cards that cost VALUE or less. -1 if it has no such condition
|costEqual|Integer|Filters cards that cost VALUE. -1 if it has no such condition
|attackMore|Integer|Filters cards with Attack equal to VALUE or more. -1 if it has no such condition
|attackLess|Integer|Filters cards with Attack equal to VALUE or less. -1 if it has no such condition
|attackEqual|Integer|Filters cards with Attack equal to VALUE. -1 if it has no such condition
|classId|Integer|Filters cards with class id VALUE. 0 if it has no such condition
|cardTypeId|Integer|Filters cards with card type id VALUE (Card types like Hero, Minion, Spell,...). 0 if it has no such condition
|raceId|Integer|Filters cards with minion type id VALUE. 0 if it has no such condition
|schoolId|Integer|Filters cards with spell school id VALUE. 0 if it has no such condition
|rarityId|Integer|Filters cards with rarity id VALUE. 0 if it has no such condition
|bg_isGolden|Integer|1 if it only generates golden cards in Battlegrounds, 0 otherwise
|keywordTagId|Integer|Filters cards that have tag id VALUE considered keywords. 0 if it has no such condition
|tagId|Integer|Filters cards that have tag id VALUE. 0 if it has no such condition
|tagValue|Integer|Filters cards that have tag id VALUE, with its value equal to a certain amount. -1 if there is no need to specify the value for tagId
|isFromThePast|Integer|1 to filter Wild-only cards, 0 otherwise
|isForGenerating|Integer|1 if it is for generating, 0 otherwise
|isCostVaried|Integer|1 if it has Cost condition, but it is not fixed (like Nethrandamus), 0 otherwise
|dependsTarget|Integer|1 if it depends on target to filter cards (like Amalgam of the Deep), 0 otherwise
|dependsCurrentClass|Integer|1 if it depends on your hero's class (mostly for Discover cards), 0 otherwise
|requiresAnotherClass|Integer|1 if it chooses cards from class different to your hero's or played card's (mostly for Rogue cards), 0 otherwise
|dependsFormat|Integer|1 if the pool varies between Constructed formats, 0 otherwise
|bg_dependsCurrentTier|Integer|1 if it depends on your Battlegrounds Tavern Tier, 0 otherwise
|additionalPoolDbfIds|Array of Integer|List of dbfIds hard-defined by Wiki. Cards with these dbfIds will always be available in this pool no matter how the conditions are factored
|wikiBanPoolIds|Array of Integer|List of WikiBanPool ids hard-defined by Wiki. This pool will consider these ban pools to exclude the mentioned cards from its pool
