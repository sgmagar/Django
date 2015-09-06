from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone

#session
from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
session = SessionStore()

from .models import Question, Answer_Choice, Score
import random

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]

	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))
		

def detail(request):
	template = loader.get_template('quiz/detail.html')
	
	request.session['question_no'] +=1
	if request.session['question_no'] == 6:
		return HttpResponseRedirect(reverse('quiz:results'))
	key = random.randint(1,8)
	while True:
		i=0
		for value in request.session['question_list']:
			i+=1
			if value==key:
				key =random.randint(1,8)
				break
		if i == len(request.session['question_list']):
				break

	request.session['question_list'].append(key)
	#question = Question.objects.filter(pk=key)
	question = get_object_or_404(Question, pk=key)
	context = RequestContext(request, {
		'question': question,
		'question_no': request.session['question_no']
	})
	print question
	return HttpResponse(template.render(context))

		
def results(request):
	
	template = loader.get_template('quiz/results.html')
	
	#score = Score.objects.filter(id=request.session['user_id'])
	score = get_object_or_404(Score, pk=request.session['user_id'])
	context= RequestContext(request, {
		'score':score
	})
	return HttpResponse(template.render(context))

def login(request):
	template = loader.get_template('quiz/login.html') 
	context = RequestContext(request, {

	})
	return HttpResponse(template.render(context))

def score(request):
	#first
	#return HttpResponse("You're voting on question %s." % question_id)
	#p = Question.objects.filter(pk=2)
	user = get_object_or_404(Score, pk=request.session['user_id'])
	try:
		#selected_choice = p.answer_choice_set.get(choice_correct=request.POST['choice'])
		answer = str(request.POST['choice'])

	except :
	#except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form.
		return render(request, 'quiz/detail.html', {
			'error_message': "You didn't select a choice",
			})
	else:
		
		#selected_choice.votes+=1
		if answer=='True':
			user.score += 1
			user.save()
		return HttpResponseRedirect(reverse('quiz:detail'))



		#selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		
def addlogin(request):
	#p = Question.objects.get(pk=3)
	try:
		score = Score(username=request.POST['username'])
	except :
		return HttpResponseRedirect(reverse('quiz:login'))
	else:

		score.save()
		request.session['question_no'] = 0
		request.session['user_id'] = score.id
		request.session['question_list'] = []
		return HttpResponseRedirect(reverse('quiz:detail'))

	
	
