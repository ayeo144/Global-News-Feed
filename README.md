# Global News Feed

## Design

### Data Pipeline

#### Extracting "Raw" Data

News headline data is extracted from an [API](https://newsapi.org/) in JSON format.

![Alt text](https://github.com/ayeo144/Global-News-Feed/blob/main/docs/images/ETL_Architecture.png?raw=true)

#### Raw Data Storage

Raw data from the API is stored in JSON format in file structure allowing for it to be easily accessible. 
Each JSON file contains the news headlines for one country and is named appropriately, e.g. `Australia.json`. 
Requests are made at given time intervals, and news headlines extracted for specified countries. The JSON files
for specific request 'interval' are stored in a timestamped directory.

```
root-dir
|
|__Responses_YYYYMMDD_HHMMSS
	|
	|__countryA.json
	|
	|__countryB.json
```

The path of the timestamped directory is recorded in a table in a database for future reference, allowing the most
up-to-date set of API responses to be easily identified and accessed.

#### Loading "Raw" Data into a Database