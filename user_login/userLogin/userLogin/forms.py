from django.contrib.auth.models import User
from login.models import *
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import ModelForm

class UserForm(ModelForm):
	confirmpassword= forms.CharField(widget=forms.PasswordInput(attrs={'name':'confirmpassword','id':'confirmpassword','class':'form-control input-area','placeholder':'Confirm Password','autofocus':'autofocus'})) 

	class Meta:
		model=User
		fields=['username','email','first_name','last_name','password']
		widgets={
			'username': forms.TextInput(attrs={'name':'username','id':'username','class':'form-control input-area','placeholder':'Username','autofocus':'autofocus'}),
			'email': forms.EmailInput(attrs={'name':'email','id':'email','class':'form-control input-area','placeholder':'Email','autofocus':'autofocus'}),
			'first_name': forms.TextInput(attrs={'name':'firstname','id':'firstname','class':'form-control input-area','placeholder':'First Name','autofocus':'autofocus'}),
			'last_name': forms.TextInput(attrs={'name':'lastname','id':'lastname','class':'form-control input-area','placeholder':'Last Name','autofocus':'autofocus'}),
			'password': forms.PasswordInput(attrs={'name':'password','id':'password','class':'form-control input-area','placeholder':'Password','autofocus':'autofocus'})
		}
	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		username = cleaned_data.get("username")
		email = cleaned_data.get("email")
		firstname = cleaned_data.get("first_name")
		lastname = cleaned_data.get("last_name")
		password = cleaned_data.get("password")
		confirmpassword =cleaned_data.get("confirmpassword")
		if password != confirmpassword:
			msg = 'Both password should watch'
			self.add_error('confirmpassword',msg)
		if email == "":
			msg = "This field is required"
			self.add_error('email',msg)
		return cleaned_data
		# if username == "":
		# 	raise forms.ValidationError("Username can't be empty")

class UserProfileForm(ModelForm):
	class Meta:
		model=UserProfile
		fields=['gender','holiday_date','website']
		# exclude=['user']
		widgets={
			'website':forms.TextInput(attrs={'name':'website','id':'website','class':'form-control input-area','placeholder':'Website','autofocus':'autofocus'}),
			'gender':forms.Select(attrs={'class':'form-control'}),
			'holiday_date':DateTimePicker(options={"format": "YYYY-MM-DD"}),
		}

	def clean(self):
		cleaned_data = super(UserProfileForm,self).clean()
		website = cleaned_data.get("website")


