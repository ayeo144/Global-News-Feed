# Global News Feed

A simple project demonstrating components of data engineering and "full-stack" web development.

The concept (stil under development!) is a web app/site/page with an interactive map displaying top news headlines from different countries.

## Design

The project contains two core components. 

1. The data engineering component, where ETL scripts are used to populate the database with news headline information.
2. The web app component, which contains a backend server and a frontend displaying the data to the user.

[ETL](https://github.com/ayeo144/Global-News-Feed/blob/main/etl/README.md)
[Backend](https://github.com/ayeo144/Global-News-Feed/blob/main/backend/README.md)
[Frontend](https://github.com/ayeo144/Global-News-Feed/blob/main/frontend/README.md)

The project is fully containerised, and the `docker-compose` file can be used to create all required services for running the web application.