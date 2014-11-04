stopSound
=========

Stopsound is the engineering project for the Theta Tau Nu Pledge class.
Stopsound is a Raspberry Pi app that monitors the sound level in your room 
and sends out text messages to alert your neighbors to quiet down.

This is the Django web app that manages your contacts and settings for Stop Sound. It acts as a contact store that allows you to easily activate and deactivate the people you want to send text messages to. 

We deployed this application on heroku. View it [here](stopsound.herokuapp.com)


Setting up your Dev Environmnet
-------------------------------
Theta Tau Nu's Pledge Class Engineering Project

First, create a [virtualenv](http://virtualenv.readthedocs.org/en/latest/).
Look into [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) to make virtualenv much more convienent and better.

Next: make sure you have bower installed via [bower.io](http://bower.io). NOTE/TODO: THIS IS NOT NECESSARY BECAUSE I DONT KNOW HOW TO USER BOWER ON HEROKU.
Note, this may require you to download and install [node.js](http://nodejs.org).

Then: activate the virtual environment. If you are using virtualenvwrapper:
  
    workon ENVNAME

Otherwise, in the directory where you installed your virtualenv, run:

    source ENVNAME/bin/activate

To install the dependencies:

  1. Install the requiremnts in requiremnets.txt w/ your virtualenv activated.

         pip install -r requirements.txt

  2. Install the javascript dependecies in `static/` by running (Not necessary atm)

         bower install

Because we are deploying this app to Heroku, we use [foreman](https://github.com/ddollar/foreman) to load environmental variables, especially the Twilio 
account information. Make sure to include a .env defining TWILIO\_SID, TWILIO\_TOKEN, and TWILIO\_NUMBER in the format:
  
    TWILIO_TOKEN="AUTH TOKEN"
    
Then, we need to setup our Django database. Because our dataset is going to be relatively small, we use SQLite. The following commands sets up your database.

    python manage.py syncdb
    python manage.py migrate

To test out the django app locally:

    make runserver 

To play around in the django shell:

    make shell 

TODO LIST:
---------
1. Change local database from SQLite to Postgres since Heroku uses Postgres
2. Differ between dev and production settings.
3. Attach Users to contacts
4. Use fuzzy matching to determine if new user has a profile already in list.
5. Prettify the app. It looks like every Bootstrap app. No images and what not.
