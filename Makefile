env:
	sudo apt install python3-pip
	pip3 install virtualenv
	python3 -m venv env

install: requirements.txt 
	pip3 install -r requirements.txt 

scrape:
ifdef n
	python manage.py scrape --n=$(n)
else
	python manage.py scrape
endif

signup:
# make create n=$$n
ifdef n
	python manage.py signup --n=$(n)
else
	python manage.py signup
endif

