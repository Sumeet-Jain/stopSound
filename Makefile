install_reqs:
	sudo apt-get install python-pyaudio;
	easy_install pygooglevoice
	pip install -r requirements.txt;
	cd stopSound/static && bower install
