from __future__ import absolute_import
import csv
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import user_passes_test
from .site_crawler import *
from .handle_csv import *
from .forms import *
from fundraising.models import *

import json
import os
import locale
locale.setlocale(locale.LC_ALL,'')

file = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/original_fund.csv'

def home(request):
    total = AllData.objects.all().aggregate(total=Sum('amount'))['total']
    international = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    national = AllData.objects.filter(donorCountry__iexact="NEPAL").aggregate(national=Sum('amount'))['national']
    crowdFunding = Fundraiser.objects.all().aggregate(crowdFunding=Sum('raised'))['crowdFunding']
    if crowdFunding == None:
        crowdFunding=0
    international_subcategory = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    national_subcategory = AllData.objects.filter(donorCountry__iexact="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    crowdFundingSubcategory = Fundraiser.objects.all().order_by('-raised')
    for items in international_subcategory:
        items['percent'] = (float(items['agg_amount'])/float(international))*100
        print items
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in national_subcategory:
        items['percent'] = (float(items['agg_amount'])/float(national))*100
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)

    for items in crowdFundingSubcategory:
        items.percent = (float(items.raised)/float(crowdFunding))*100
        items.raised = locale.currency(items.raised,grouping=True)
    
    context={
        "title": "Home",
        "total": locale.currency((total+crowdFunding), grouping=True),
        "international": locale.currency(international, grouping=True),
        "national": locale.currency(national, grouping=True),
        "international_subcategory": international_subcategory,
        "national_subcategory": national_subcategory,
        "crowdFunding": locale.currency(crowdFunding, grouping=True),
        "crowdFundingSubcategory": crowdFundingSubcategory
    }
    # table_csv(file)
    return render(request,"index.html",context)

def about(request):
    context={
        "title": "About"
    }
    return render(request, "about.html",context)

def aids(request):
    total = AllData.objects.all().aggregate(total=Sum('amount'))['total']
    international = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    national = AllData.objects.filter(donorCountry__iexact="NEPAL").aggregate(national=Sum('amount'))['national']
    international_subcategory = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    national_subcategory = AllData.objects.filter(donorCountry__iexact="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    crowdFunding = Fundraiser.objects.all().aggregate(crowdFunding=Sum('raised'))['crowdFunding']
    if crowdFunding == None:
        crowdFunding=0
    for items in international_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in national_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    international_percent = (float(international)/float(total+crowdFunding))*100
    national_percent = (float(national)/float(total+crowdFunding))*100
    crowdFunding_percent = (float(crowdFunding)/float(total+crowdFunding))*100
    context={
        "title": "Aids",
        "total": locale.currency(total, grouping=True),
        "international": locale.currency(international, grouping=True),
        "national": locale.currency(national, grouping=True),
        "crowdFunding": locale.currency(crowdFunding, grouping=True),
        "international_subcategory": international_subcategory,
        "national_subcategory": national_subcategory,
        "international_percent": international_percent,
        "national_percent": national_percent,
        "crowdFunding_percent": crowdFunding_percent
    }
    # table_csv(file)

    return render(request, 'aids.html',context)

def infographics(request):
    context={
        "title": "Infographics",
        "value": 55
    }
    return render(request, 'infographics.html',context)

def provideaidinfo(request):
    context={
        "title": "Provide Aid Info"
    }
    if request.POST:
        donorName = request.POST['donorName'].strip()
        donorWebsite = request.POST['donorWebsite'].strip()
        donorType = request.POST['donorType'].strip()
        donorCountry = request.POST['donorCountry'].strip()
        recipientName = request.POST['recipientName'].strip()
        recipientWebsite = request.POST['recipientWebsite'].strip()
        recipientType = request.POST['recipientType'].strip()
        recipientCountry = request.POST['recipientCountry'].strip()
        transactionDate = request.POST['transactionDate'].strip()
        amount = request.POST['amount'].strip()
        if amount=='':
            amount=0
        else:
            amount=float(amount)
        currency = request.POST['currency'].strip()
        aidType = request.POST['aidType'].strip()
        transactionType = request.POST['transactionType'].strip()
        description = request.POST['description'].strip()
        source = request.POST['source'].strip()
        links = request.POST['links'].strip()
        sector = request.POST['sector'].strip()
        targetGeography = request.POST['targetGeography'].strip()
        vdc = request.POST['vdc'].strip()
        # print donorName,donorWebsite,donorType,donorCountry,recipientName,recipientWebsite,recipientType,recipientCountry,\
        #     transactionDate,amount,currency,aidType,transactionType,description,source,links,sector,targetGeography,vdc
        aidsData = AidsData(donorName=donorName,donorWebsite=donorWebsite,donorType=donorType,donorCountry=donorCountry,\
            recipientName=recipientName,recipientWebsite=recipientWebsite,recipientType=recipientType,\
            recipientCountry=recipientCountry,transactionDate=transactionDate,amount=amount,currency=currency,\
            aidType=aidType,transactionType=transactionType,description=description,source=source,links=links,\
            sector=sector,targetGeography=targetGeography,vdc=vdc)
        aidsData.save()

    return render(request, 'provideaidinfo.html',context)

def aidsdetailsint(request,subcat):
    if subcat=='I':
        subcat='I/NGOs'
    international = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    national = AllData.objects.filter(donorCountry__iexact="NEPAL").aggregate(national=Sum('amount'))['national']
    international_subcategory = AllData.objects.all().exclude(donorCountry="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    national_subcategory = AllData.objects.filter(donorCountry__iexact="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    subcat_total = AllData.objects.exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").filter(donorType=subcat).aggregate(total_subcat=Sum('amount'))['total_subcat']
    data = AllData.objects.exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").filter(donorType=subcat).order_by('-amount')
    for items in international_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in national_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in data:
        items.percent =(float(items.amount)/float(subcat_total))*100 
        # items.donorName=items.donorName.replace(" ","")
        # print type(items.donorName)
        items.amount= locale.currency(items.amount, grouping=True)
    context={
        "title": "Aids Details Int",
        "type": subcat,
        "subcat_total": locale.currency(subcat_total, grouping=True),
        "data": data,
        "international": locale.currency(international, grouping=True),
        "national": locale.currency(national, grouping=True),
        "international_subcategory": international_subcategory,
        "national_subcategory": national_subcategory
    }
    return render(request, 'aidsdetails-int.html',context)

def aidsdetailsgov(request, subcat):
    if subcat=='I':
        subcat='I/NGOs'
    international = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    national = AllData.objects.filter(donorCountry__iexact="NEPAL").aggregate(national=Sum('amount'))['national']
    international_subcategory = AllData.objects.all().exclude(donorCountry="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    national_subcategory = AllData.objects.filter(donorCountry="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    subcat_total = AllData.objects.filter(donorCountry__iexact="NEPAL",donorType=subcat).aggregate(total_subcat=Sum('amount'))['total_subcat']
    data = AllData.objects.filter(donorCountry__iexact="NEPAL",donorType=subcat).order_by('-amount')
    for items in international_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in national_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in data:
        items.percent =(float(items.amount)/float(subcat_total))*100 
        # items.donorName=items.donorName.replace(" ","")
        items.amount= locale.currency(items.amount, grouping=True)
    print subcat
    context={
        "title": "Aids Details Gov",
        "type": subcat,
        "subcat_total": locale.currency(subcat_total, grouping=True),
        "data": data,
        "international": locale.currency(international, grouping=True),
        "national": locale.currency(national, grouping=True),
        "international_subcategory": international_subcategory,
        "national_subcategory": national_subcategory
    }
    return render(request, 'aidsdetails-gov.html',context)

def bydonorname(request):
    donorName = request.POST['search']
    donorNameSum = AllData.objects.filter(donorName__iexact=donorName).aggregate(donorNameSum=Sum('amount'))['donorNameSum']
    if donorNameSum==None:
        donorNameSum=0
    donorNameList = AllData.objects.filter(donorName__iexact=donorName).order_by('-amount')
    international = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    national = AllData.objects.filter(donorCountry__iexact="NEPAL").aggregate(national=Sum('amount'))['national']
    international_subcategory = AllData.objects.all().exclude(donorCountry="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    national_subcategory = AllData.objects.filter(donorCountry__iexact="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    for items in international_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in national_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in donorNameList:
        items.percent = (float(items.amount)/float(donorNameSum))*100
        items.amount = locale.currency(items.amount,grouping=True)
    context={
        "title": "Aids Details",
        "international": locale.currency(international, grouping=True),
        "national": locale.currency(national, grouping=True),
        "international_subcategory": international_subcategory,
        "national_subcategory": national_subcategory,
        "type": donorName,
        "subcat_total":locale.currency(donorNameSum, grouping=True),
        "data": donorNameList,
        "title": "Donor List By donorName"
    }

    return render(request, 'aidsdetails-int.html',context)


def aidsdetails(request, donor_id):
    international = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    national = AllData.objects.filter(donorCountry__iexact="NEPAL").aggregate(national=Sum('amount'))['national']
    international_subcategory = AllData.objects.all().exclude(donorCountry="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    national_subcategory = AllData.objects.filter(donorCountry__iexact="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    donorObject = AllData.objects.get(id=donor_id);
    for items in international_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    for items in national_subcategory:
        items['agg_amount'] = locale.currency(items['agg_amount'],grouping=True)
    donorObject.amount = locale.currency(donorObject.amount,grouping=True)
    context={
        "title": "Aids Details",
        "international": locale.currency(international, grouping=True),
        "national": locale.currency(national, grouping=True),
        "international_subcategory": international_subcategory,
        "national_subcategory": national_subcategory,
        "donorObject": donorObject
    }
    return render(request, 'aidsdetails.html',context)

def infographdataint(request):
    international = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    # national = AllData.objects.filter(donorCountry="NEPAL").aggregate(national=Sum('amount'))['national']
    international_subcategory = AllData.objects.all().exclude(donorCountry__iexact="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
     # national_subcategory = AllData.objects.filter(donorCountry="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    dataInt = []
    for items in international_subcategory:
        donorType = items['donorType']
        percent = (float(items['agg_amount'])/float(international))*100
        donor = {}
        donor['donorType']=donorType
        donor['percent']=percent
        dataInt.append(donor)
        print donorType,percent
    data={'intdata':dataInt}
    data = json.dumps(data)
    return HttpResponse(data)

def infographdatagov(request):
    # international = AllData.objects.all().exclude(donorCountry="NEPAL").exclude(donorCountry="").aggregate(international=Sum('amount'))['international']
    national = AllData.objects.filter(donorCountry__iexact="NEPAL").aggregate(national=Sum('amount'))['national']
    # international_subcategory = AllData.objects.all().exclude(donorCountry="NEPAL").exclude(donorCountry="").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    national_subcategory = AllData.objects.filter(donorCountry__iexact="NEPAL").values('donorType').annotate(agg_amount=Sum('amount')).order_by(Sum('amount').desc())
    dataGov = []
    for items in national_subcategory:
        donorType = items['donorType']
        percent = (float(items['agg_amount'])/float(national))*100
        donor = {}
        donor['donorType']=donorType
        donor['percent']=percent
        dataGov.append(donor)
        print donorType,percent
    data={'govdata':dataGov}
    data = json.dumps(data)
    return HttpResponse(data)
def infographdatacrowd(request):
    crowdFunding = Fundraiser.objects.all().aggregate(crowdFunding=Sum('raised'))['crowdFunding']
    crowdFundingSubcategory = Fundraiser.objects.all()
    dataCrowd = []
    for items in crowdFundingSubcategory:
        fundraiser = items.fundraiser
        percent = (float(items.raised)/float(crowdFunding))*100
        fundraised = {}
        fundraised['fundraiser'] = fundraiser
        fundraised['percent'] = percent
        dataCrowd.append(fundraised)
    data = {'crowddata':dataCrowd}
    data = json.dumps(data)
    return HttpResponse(data)


############################################functions############################################

def table_csv(file):
    data = csv.DictReader(open(file))
    for row in data:
        donorName = row['Donor Name'].strip()
        donorWebsite = row['Donor Website'].strip()
        donorType = row['Donor Type'].strip()
        donorCountry = row['Donor Country'].strip()
        recipientName = row['Recipient Name'].strip()
        recipientWebsite = row['Recipient Website'].strip()
        recipientType = row['Recipient Type'].strip()
        recipientCountry = row['Recipient Country'].strip()
        transactionDate = row['Transaction Date'].strip()
        amount = row['Amount'].strip()
        if amount=='':
            amount=0
        else:
            amount=float(amount)
        currency = row['Currency'].strip()
        aidType = row['Aid Type'].strip()
        transactionType = row['Transaction Type'].strip()
        description = row['Description'].strip()
        source = row['Source'].strip()
        links = row['Links'].strip()
        dateType = row['Date Type'].strip()
        date = row['Date'].strip()
        sector = row['Sector'].strip()
        targetGeography = row['Target Geography'].strip()
        vdc = row['VDC'].strip()
        allData = AllData(donorName=donorName,donorWebsite=donorWebsite,donorType=donorType,donorCountry=donorCountry,\
            recipientName=recipientName,recipientWebsite=recipientWebsite,recipientType=recipientType,\
            recipientCountry=recipientCountry,transactionDate=transactionDate,amount=amount,currency=currency,\
            aidType=aidType,transactionType=transactionType,description=description,source=source,links=links,\
            dateType=dateType,sector=sector,targetGeography=targetGeography,vdc=vdc)
        allData.save()
        
        


