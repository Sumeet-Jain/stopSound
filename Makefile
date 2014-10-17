install_reqs:
	sudo apt-get install python-pyaudio;
	pip install -r requirements.txt;
	cd stopSound/static && bower install

runserver: 
	foreman run python manage.py runserver

shell:
	foreman run python manage.py shell

migrate:
	foreman run python manage.py migrate

syncdb:
	foreman run python manage.py syncdb
