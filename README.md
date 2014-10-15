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

Otherwise:

  1. Install [pyaudio](http://people.csail.mit.edu/hubert/pyaudio/)

  2. Install the requiremnts in requiremnets.txt w/ your virtualenv activated.

         pip install -r requirements.txt

  3. Install the javascript dependecies in `stopSound/static/` by running:

         bower install
    
Then, we need to setup our Django database. Because our dataset is going to be relatively small, we use SQLite. The following commands sets up your database.

    python manage.py syncdb
    python manage.py migrate

To test out the django app locally:

    python manage.py runserver

To play around in the django shell:

    python manage.py shell
