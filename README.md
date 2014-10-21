stopSound
=========

Theta Tau Nu's Pledge Class Engineering Project

First, create a [virtualenv](http://virtualenv.readthedocs.org/en/latest/).
Look into [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) to make virtualenv much more convienent and better.

Next: make sure you have bower installed via [bower.io](http://bower.io). 
Note, this may require you to download and install [node.js](http://nodejs.org).

Then: activate the virtual environment. If you are using virtualenvwrapper:
  
    workon ENVNAME

Otherwise, in the directory where you installed your virtualenv, run:

    source ENVNAME/bin/activate

Because we are using Debian on our Raspberry Pi, the Makefile uses apt-get. Only run this command on Debian distro. 

     make install_reqs

Because we are deploying this app to Heroku, we use [foreman](https://github.com/ddollar/foreman) to load environmental variables, especially the Google Voice
account information. Make sure to include a .env defining `GV_EMAIL` and `GV_PW` into the app if you are using the text messaging feature.

Otherwise:

  1. Install [pyaudio](http://people.csail.mit.edu/hubert/pyaudio/)

  2. Install the requiremnts in requiremnets.txt w/ your virtualenv activated.

         pip install -r requirements.txt

  3. Install the javascript dependecies in `static/` by running:

         bower install
    
Then, we need to setup our Django database. Because our dataset is going to be relatively small, we use SQLite. The following commands sets up your database.

    python manage.py syncdb
    python manage.py migrate

To test out the django app locally:

    make runserver 

To play around in the django shell:

    make shell 

TODO LIST:
---------
0. Do the stop sound raspberry pi app
1. Change local database from SQLite to Postgres since Heroku uses Postgres
2. Figure out a better way to send text messages or get pass google login security
3. Attach Users to contacts
4. Use fuzzy matching to determine if new user has a profile already in list.
5. Prettify the app. It looks like every Bootstrap app
