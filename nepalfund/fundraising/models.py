from django.db import models



class AllData(models.Model):
    donorName = models.CharField(max_length=200)
    donorWebsite = models.URLField(blank=True)
    donorType = models.CharField(max_length=100)
    donorCountry = models.CharField(max_length=50)
    recipientName = models.CharField(max_length=70, blank=True)
    recipientWebsite = models.URLField(blank=True)
    recipientType = models.CharField(max_length=100,blank=True)
    recipientCountry = models.CharField(max_length=70, blank=True)
    transactionDate = models.CharField(max_length=40, blank=True)
    amount = models.DecimalField(default=True, max_digits=15,decimal_places=2)
    currency = models.CharField(max_length=20,blank=True)
    aidType = models.CharField(max_length=20)
    transactionType = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=100,blank=True)
    links = models.URLField(blank=True)
    dateType = models.CharField(max_length=20, blank=True)
    date = models.CharField(max_length=10,blank=True)
    sector = models.CharField(max_length=100, blank=True)
    targetGeography = models.CharField(max_length=100, blank=True)
    vdc = models.CharField(max_length=40, blank=True) 

class AidsData(models.Model):
    donorName = models.CharField(max_length=200)
    donorWebsite = models.URLField(blank=True)
    donorType = models.CharField(max_length=100)
    donorCountry = models.CharField(max_length=50)
    recipientName = models.CharField(max_length=70, blank=True)
    recipientWebsite = models.URLField(blank=True)
    recipientType = models.CharField(max_length=100,blank=True)
    recipientCountry = models.CharField(max_length=70, blank=True)
    transactionDate = models.CharField(max_length=40, blank=True)
    amount = models.DecimalField(default=True, max_digits=15,decimal_places=2)
    currency = models.CharField(max_length=20,blank=True)
    aidType = models.CharField(max_length=20)
    transactionType = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=100,blank=True)
    links = models.URLField(blank=True)
    dateType = models.CharField(max_length=20, blank=True)
    date = models.CharField(max_length=10,blank=True)
    sector = models.CharField(max_length=100, blank=True)
    targetGeography = models.CharField(max_length=100, blank=True)
    vdc = models.CharField(max_length=40, blank=True) 

class Fundraiser(models.Model):
    fundraiser = models.CharField(max_length=30, blank=True)
    url = models.URLField(blank=True)
    raised = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.fundraiser

