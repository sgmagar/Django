
Requirements:
	python 2.7
	Django 1.8

Procedures to run application:
	1>Clone to you computer or download zip
	2>cd to Django/innoseva
	3>run python manage.py runserver
		This will run the server. Then go to localhost:8000 in your browser.
	4>Enter firstname, lastname, contact no, and upload csv file.
		csv file contains the header:
			firstname,lastname,phonenumber,address
		if your entered detail is in the csv file, then you will get Message:
			Welcome to the site
		and if your entered detail is not in the csv file, then you will get:
			Sorry we,don't recognize you
		and if you didnot entered any detail and did not upload file, then you will get:
			Sorry we,don't recognize you
		if you upload any other file then csv, then you will get:
			Sorry we don't recognize you. Please upload csv file.
	