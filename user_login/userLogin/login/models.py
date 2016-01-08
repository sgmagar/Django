from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
today = date.today()

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female'),
		)
	gender = models.CharField(default='M',max_length=1, choices=GENDER_CHOICES)
	holiday_date = models.DateField(default=timezone.now())

	def __unicode__(self):
		return self.user.username