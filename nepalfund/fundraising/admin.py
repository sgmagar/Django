from django import forms
from django.contrib import admin
from fundraising.models import *
import csv


class AllDataAdmin(admin.ModelAdmin):
    fields = ('donorName','donorWebsite','donorType','donorCountry','recipientName','recipientWebsite','recipientType',
        'recipientCountry','transactionDate','amount','currency','aidType','transactionType','description','source',
        'links','dateType','date','sector','targetGeography','vdc')
    list_display = ('donorName','donorWebsite','donorType','donorCountry','transactionDate','amount')
    search_fields = ['donorCountry','donorType','donorName','transactionDate']

class AidsDataAdmin(admin.ModelAdmin):
    fields = ('donorName','donorWebsite','donorType','donorCountry','recipientName','recipientWebsite','recipientType',
        'recipientCountry','transactionDate','amount','currency','aidType','transactionType','description','source',
        'links','dateType','date','sector','targetGeography','vdc')
    list_display = ('donorName','donorWebsite','donorType','donorCountry','recipientName','recipientWebsite','recipientType',
        'recipientCountry','transactionDate','amount','currency','aidType','transactionType','description','source',
        'links','dateType','date','sector','targetGeography','vdc')
    search_fields = ['donorCountry','donorType','donorName','transactionDate']




class FundraiserAdmin(admin.ModelAdmin):
    list_display = ('fundraiser', 'url', 'raised')
    search_fields = ['fundraiser', 'url', 'raised']



