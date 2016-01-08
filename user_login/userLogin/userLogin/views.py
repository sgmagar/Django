from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from login.models import *
from .forms import *


def home(request):
	return redirect(reverse('register'))

def register(request):
	if request.method == 'POST':
		userform = UserForm(request.POST)
		profileform = UserProfileForm(request.POST)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save(commit=False)
			user.set_password(userform.cleaned_data['password'])
			user.save()
			userprofile = profileform.save(commit=False)
			userprofile.user = user
			userprofile.save()
			return redirect(reverse('home'))
		context={
			"userForm":userform,
			"userProfileForm":profileform
		}
	else:
		userForm = UserForm()
		userProfileForm = UserProfileForm()
		context={
			"userForm":userForm,
			"userProfileForm": userProfileForm
		}
	return render(request,'index.html',context)

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponse('Welcome to the site ' + username)
		else:
			context={
				'error':'Username or Password Invalid'
			}

	else:
		context={}
	return render(request,'login.html',context)
@login_required(login_url='login')
def restricted(request):
	return HttpResponse('This is restricted')
@login_required(login_url='login')
def logout_view(request):
	logout(request)
	return redirect(reverse('home'))