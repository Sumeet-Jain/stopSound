install_reqs:
	sudo apt-get install python-pyaudio;
	pip install -r requirements.txt;
	cd stopSound/static && bower install
