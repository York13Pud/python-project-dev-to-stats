# Project Requirements

## Backend

* Create an API key on dev.io to be used for making API calls
  * Use only the data that is available via the dev.io API
* Collect a list of every article on dev.to that a user has created
* Store each articles details in a SQL database
  * If the article is already in the database, don't add it again
* Every hour (actual time to be determined), make a call to the dev.to API to gather the articles
  * Store the number of comments and likes in a SQL database

### Tools to use

* Python and additional libraries
* FastAPI or Flask (web and API framework)
* PostgreSQL (database)
* nginx (web server)

## Web Frontend

* Visualise the changes in a list with an option to switch between hour, day, week, month and yearly views
  * This list would show:
    * Article ID
    * Article title (hyperlinked to the article)
    * Total views
    * Changes in views since the last update
    * Total comments
    * Changes in views since the last update
* Optional: Present the data as graphs

### Tools to use

* HTML
* CSS / BootStrap
* JavaScript
* d3.js