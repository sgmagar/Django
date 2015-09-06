from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

class HomeView(generic.ListView):

	#model = Question
	template_name = 'home.html' 

	def get_queryset(self):
		pass