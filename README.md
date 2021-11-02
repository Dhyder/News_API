# Pandora News
## Author
* [Dhyder](https://github.com/Dhyder)

## Description
Pandora News is a web application that displays a list of news from different news sources including the sources themselves. Upon page load, it exhibits the top news articles of the day. Clicking a news article to view source or read more, it redirects the user to read it fully from the news source itself. This is achieved by means of an api key [News API](https://newsapi.org/).

## Screenshot
![cipher](https://user-images.githubusercontent.com/86789832/139797528-3c7eba2f-b466-444e-b561-369474a53595.PNG)

## Live Link
You can view the site at: [Pandora](https://pandora-news.herokuapp.com/)

## User Stories

### As a user I would like to:
* See various news sources
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed in a list |
| Display tabs with news by category | **On Tab link click** | Clickable links to open news based on category |
| Display articles from a news source | **Click a news source** | Redirected to a page with articles from the source |
| Display the preview of an article headline | **On page load** | Each article headline displays an image,description and publication date |
| To Read more on an entire article  | **Click an article** | Redirected to the news source's site to read the entire article |


## SetUp / Installation Requirements
### Prerequisites
* python3.9
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/Dhyder/News_Api/
        $ cd News_API

## Running the Application
* Creating the virtual environment

        $ python3.9 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.9 -m pip install Flask
        $ python3.9 -m pip install Flask-bootstrap
        $ python3.9 -m pip install Flask-Script

* Setting up the API Key

        To be able to gather article info from the News API you will need an API Key.

        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it:

                export NEWS_API_KEY='<Your-Api-Key>'
                python3.9 manage.py server

        * Insert the API Key you received from News Api where <Your-Api-Key> is.

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.9 manage.py tests

## Technologies Used
* Python3.9.2
* Flask

## Known Bugs
* No known bugs at the moment
## Author's Contact Information
* For any queries, you can reach out at [desastrecaliente@gmail.com]

### MIT License:
Copyright (c) 2021 **Dhyder**

