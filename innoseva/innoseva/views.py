from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader


import os
import csv

path=os.path.dirname(__file__)
uploaded_file_path=path[:-8] + "static/uploaded_files/"



def user(request):
	try:
		
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		contactno = request.POST['contactno']
		address = request.POST['address']
		try:
			uploaded_filename = request.FILES['file'].name
		except :
			pass
			name=''
		else:
			if uploaded_filename[-3:] != "csv":
				name="Please upload csv file"	
			else:
				name=''
				handle_uploaded_file(request.FILES['file'])
		check = check_existance(firstname,lastname,contactno,address)
		if check==True:
			message="Welcome to the site"
		elif check==False:
			message="Sorry we don't recognize you"

	except:
		context = RequestContext(request, {
		'title': 'Innoseva' ,
		# 'path': 'hlloe',
		
		})
	else:
		context = RequestContext(request, {
		'title': 'Innoseva' ,
		'path': name,
		'message': message,
		

		})
	template = loader.get_template('index.html')
	
	return HttpResponse(template.render(context))
	
def handle_uploaded_file(f):
	with open(uploaded_file_path + 'data.csv', 'wb+') as dest:
		for chunk in f.chunks():
			dest.write(chunk)

		#with open(f, 'rb+') as src:
			#data = src.read()
			#dest.write(data)
def check_existance(firstname,lastname,contactno,address):
	data = csv.DictReader(open(uploaded_file_path+'data.csv'))
	for row in data:
		first_name = row['firstname']
		last_name = row['lastname']
		contact_no = row['phonenumber']
		contact_address = row['address']

		if first_name==firstname and last_name==lastname and \
			contact_no==contactno and contact_address==address:
			return True

	return False
	

