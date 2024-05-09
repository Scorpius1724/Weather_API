# Weather API
## Rest API to query historical temperature data across Europe.
## Description:
#### This is a rest API that allows the user to query historical temperature data (for about the last 200 years or more) recorded across various weather stations present in Europe. The data was collected by the EUROPEAN CLIMATE ASSESSMENT & DATASET (ECA&D). The project is written in HTML and Python using the Flask web framework. The pandas Python library is used to sort through the raw weather data.
## Tech Stacks:
#### HTML, Python, PyCharm IDE, Flask framework, Git, Pandas library
## Usage guide:
* #### To query for data at a specific weather station for a specific date, you can use the URL format - ```http://127.0.0.1:5000/api/v1/<station>/<date>```. For example, to search for data recorded at station 10 on 25th October, 1988, the query URL should be ```http://127.0.0.1:5000/api/v1/10/1988-10-25```.
* #### To query for data recorded by a specific weather station for every available day, the URL query format will be ```http://127.0.0.1:5000/api/v1/<station>```.
* #### To query for data recorded by a specific weather station for a specific year, you can use the URL format - ```http://127.0.0.1:5000/api/v1/yearly/10/198```.
## Contributing: To contribute to this project, follow these steps:
* #### Fork the repository to your GitHub account.
* #### Create a new branch from the master branch for each new feature or bug fix.
* #### Make your changes within the branch, ensuring that your code adheres to our coding standards and guidelines.
* #### Test your changes thoroughly to ensure they work as expected.
* #### Commit your changes with descriptive commit messages.
* #### Push your branch to your forked repository.
* #### Submit a pull request (PR) to the main branch of the original repository.
## Reporting Bugs and Issues - 
#### If you encounter a bug or issue, please submit a new issue on our GitHub repository. Provide detailed information about the problem, including steps to reproduce it and any relevant error messages or screenshots.
## New features:
#### If you want any new feature, you can suggest them to us in our issues tab.
## License: None