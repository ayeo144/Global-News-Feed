# ETL

Code for handling data extraction from third-party sources and maintaining
the data used in the project.

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

## Notes

* When using secrets in Github Actions, remember to use `\` before any special characters (e.g. `$`, `.`) otherwise
they will not be properly loaded.

## AWS Cheat-Sheet

Commands I frequently needed to use...

1. Connecting to EC2 instance from Windows command:
	* ssh -i path/to/private-key.pem ubuntu@ec2-public-dns

2. Configuring AWS CLI:
	* aws configure

3. Logging in to AWS ECR on an EC2 instance, and configuring Docker to pull images from ECR:
	* aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com