stopSound
=========

Theta Tau Nu's Pledge Class Engineering Project

First, create a (virtualenv)[http://virtualenv.readthedocs.org/en/latest/].
Also, look into virtualenvwrapper to make the syntax of virutal env so much better (http://virtualenvwrapper.readthedocs.org/en/latest/)

Next: make sure you have bower installed (bower.io)[https://bower.io]

Then: activate the virtual environment.

If running Debian, then run:
  $ make install_reqs

Else:
  install pyaudio (http://people.csail.mit.edu/hubert/pyaudio/)
  install the requiremnts in requiremnets.txt w/ your virtualenv activated.
    $ pip install -r requirements.txt
  Finally, install the javascript dependecies in stopSound/static/ by running:
    $ bower install
    
Then to run the django app locally:
  python manage.py syncdb
  python manage.py migrate
