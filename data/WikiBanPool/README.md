# WikiBanPool
Pools of banned cards. Used with WikiCardPool
|Key|Data Type|Description
|----| ----|----
|id|Integer|Wiki identifier, served as primary key
|mockupName|String|Wiki's internal string to describe the usage of the pool
|sectionName|String|Official pool name, displayed on Wiki articles
|description|Wikistring|Pool description, displayed on Wiki articles
|gameMode|Integer|0: Invalid, 1: Constructed / Traditional, 3: Battlegrounds, 5: Mercenaries. Mainly for image display.
|dbfIds|Array of Integer|List of dbfIds hard-defined or queried by Wiki. Cards with these dbfIds will not be available in included WikiCardPools no matter how the conditions are factored
|build|Integer|Patch build number where Wiki last checked and updated
|refs|Array of Wikistring|References to confirm the banned pool is correct and up-to-date
