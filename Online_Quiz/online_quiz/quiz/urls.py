from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	# ex: /polls/5/
	url(r'^detail$', views.detail, name='detail'),
	# ex: /polls/5/results/
	url(r'^results$', views.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^score$', views.score, name='score'),
	url(r'^login$', views.login, name='login'),
	url(r'^addlogin$', views.addlogin, name='addlogin'),

]