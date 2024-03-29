# FlaskBlog
####  This is a web app that allows writers to write articles and delete articles and for readers to comment on the articles,23-Sep-2019
#### By **Kingecha Kevin Nyota**
## Link to live site
You can view the site here ---> https://flask-blog254.herokuapp.com

## Description
This is a blog site created using the python flask framework it is a platform to share the skills i have learnt so far on my programming journey.
## User Stories
- [x] User can see various blog articles from various categories on the homepage of the application.
- [x] Writer can sign into the application and create an article
- [x] User can add a comment on any article
- [x] Writer can edit or delete an article in the application 
- [x] User sees random quotes displayed on the homepage

## Setup/Installation Requirements
* Ensure that Python is installed on your machine if not please visit the python website and download the latest version python 3.6
* Fork the repository and either download the project or clone it to your machine
* Create a virtual environment using the following command
```
python3.6 -m venv --without-pip virtualenv
```
* then install the latest version of pip
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
* Register the secret key as an environment variable in your terminal as follows
```
export SECRET_KEY=<your-secret-key>
```
* Regester your Email as follows in the environment
```
export MAIL_USERNAME=<Your-email>
```
* Regester your Email Password as follows in the environment
```
export MAIL_PASSWORD=<Your-email-password>
```
* run the application from your terminal using the following command
```
python3.6 manage.py server
```
* To edit the code if you will need any dependancys you will need to navigate to the virtual environment in order to install them from there to avoid version conflicts
```
source virtualenv/bin/activate
```
## Known Bugs
There are no known bug if any dont hesitate to contact me
## Technologies Used
1. Python Version 3.6
2. Flask Framework
3. Html
4. Bootstrap
5. Css
## Support and contact details
if you run into any issues please contact knyota66@gmail.com
### License
*MIT*
Copyright (c) 2019 **Kingecha Kevin Nyota**