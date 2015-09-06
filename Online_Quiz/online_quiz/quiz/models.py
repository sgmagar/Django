import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	id = models.AutoField(primary_key=True)
	question_text = models.CharField(max_length=200)
	#position = models.IntegerField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Answer_Choice(models.Model):
	id = models.AutoField(primary_key=True)
	question_id = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	correct_choice = models.BooleanField(default=False)

	def __str__(self):
		return self.choice_text
class Score(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=200)
	score= models.IntegerField(default=0)

	def __str__(self):
		return self.username



