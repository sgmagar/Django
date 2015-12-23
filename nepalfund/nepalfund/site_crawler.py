import re, urllib2
from bs4 import BeautifulSoup
from fundraising.models import *

# Crawl and parse each individual site
def parse_site(table):
    for row in table:
        url = ''
        amount = 0
        if str(row.url) == "http://www.globalgiving.org/projects/nepal-earthquake-relief-fund/":
            url = "http://www.globalgiving.org/projects/nepal-earthquake-relief-fund/"
            f = urllib2.urlopen(url)
            contents = f.read()
            soup = BeautifulSoup(contents)
            f.close()
            amount_str = soup.find('span', 'layout_abs_left').string
            amount = int(re.sub('[^\d^\.]', '', amount_str))
            soup.decompose()

        elif str(row.url) == "http://www.gofundme.com/Nepal-Earthquake-Relief/":
            url = "http://www.gofundme.com/Nepal-Earthquake-Relief/"
            f = urllib2.urlopen(url)
            contents = f.read()
            soup = BeautifulSoup(contents)
            f.close()
            amount_str = soup.find('span', 'line125').strong.string
            amount = int(re.sub('[^\d^\.]', '', amount_str))
            soup.decompose()

        elif str(row.url) == "https://life.indiegogo.com/campaign_collections/nepal-relief-fundraisers":
            url = "https://life.indiegogo.com/campaign_collections/nepal-relief-fundraisers"
            f = urllib2.urlopen(url)
            contents = f.read()
            soup = BeautifulSoup(contents)
            f.close()
            amount_str = soup.find('div', 'container-content').ul.li.next_sibling.next_sibling.next_sibling.next_sibling.span.string
            amount = int(float(re.sub('[^\d\.]', '', amount_str)) * 1000000)
            soup.decompose()

        elif str(row.url) == "https://www.crowdrise.com/Nepal-Earthquake-Relief":
            url = "https://www.crowdrise.com/Nepal-Earthquake-Relief"
            f = urllib2.urlopen(url)
            contents = f.read()
            soup = BeautifulSoup(contents)
            f.close()
            amount_str = soup.find('h3', id='total_raised_amount').string
            amount = int(re.sub('[^\d\.]', '', amount_str))
            soup.decompose()

        elif str(row.url) == "http://www.giveforward.com/organization/Nepal":
            url = "http://www.giveforward.com/organization/Nepal"
            f = urllib2.urlopen(url)
            contents = f.read()
            soup = BeautifulSoup(contents)
            f.close()
            amount_str = soup.find('h2', 'l-mg--bottom(0)').string.split('$')[1]
            amount = int(re.sub('[^\d^\.]', '', amount_str))
            soup.decompose()

        elif str(row.url) == "http://www.youcaring.com/emergency-fundraiser/relief-for-nepal-earthquake-victims/343686":
            url = "http://www.youcaring.com/emergency-fundraiser/relief-for-nepal-earthquake-victims/343686"
            f = urllib2.urlopen(url)
            contents = f.read()
            soup = BeautifulSoup(contents)
            f.close()
            amount_str = soup.find('div', 'fundraiserProgress-current').string
            amount = int(re.sub('[^\d^\.]', '', amount_str))
            soup.decompose()

        if amount != 0:
            f = Fundraiser.objects.get(url=url)
            f.raised = amount
            f.save()


# Crawler for http://www.gofundme.com/Nepal-Earthquake-Relief/ that adds data to the database
def gofundme_crawler():
    for page in range(1, 51):
        url = 'http://www.gofundme.com/Nepal-Earthquake-Relief?page=' + str(page)
        f = urllib2.urlopen(url)
        contents = f.read()
        soup = BeautifulSoup(contents)
        f.close()
        
        campaign_div = soup.find_all('div', 'search_tile')

        for div in campaign_div:
            campaign_url = div.a.get('href').strip()
            campaign_name = div.find('a', 'title').string.encode('utf-8')
            campaign_location = ''
            try:
                campaign_location = div.find('a', 'extra').string.encode('utf-8')
            except:
                campaign_location = ''
            c_total = div.find('a', 'amt').string.split(" ")
            campaign_total = int(re.sub('[^\d]', '', c_total[0]))
            campaign_donors = int(re.sub('[^\d]', '', c_total[3]))
            campaign_creator = div.find('a', 'name').string[3:].encode('utf-8')

            c_f = urllib2.urlopen(campaign_url)
            c_contents = c_f.read()
            c_soup = BeautifulSoup(c_contents)
            c_f.close()

            campaign_goal = re.sub('[^\d^\w]', '', c_soup.find('span', 'goal').string)
            campaign_created = c_soup.find('div', 'cbdate').string.replace('Created', '').strip()

            # Add to or update Database
            ob = GoFundMe.objects.filter(url=campaign_url)
            v = ob.values()
            if (not ob.exists()) or (ob.exists() and int(v[0]['donors_number']) != campaign_donors):
                obj, created = GoFundMe.objects.update_or_create(url=campaign_url, \
                    defaults={
                        'url': campaign_url, \
                        'campaign': campaign_name, \
                        'location': campaign_location, \
                        'goal': campaign_goal, \
                        'total': campaign_total, \
                        'donors_number': campaign_donors, \
                        'created_by': campaign_creator, \
                        'date_created': campaign_created})

            c_soup.decompose()

        soup.decompose()


# Update data of already created campaigns
def update_gofundme_data():
    for page in range(1, 51):
        url = 'http://www.gofundme.com/Nepal-Earthquake-Relief?page=' + str(page)
        f = urllib2.urlopen(url)
        contents = f.read()
        soup = BeautifulSoup(contents)
        f.close()

        campaign_div = soup.find_all('div', 'search_tile')

        for div in campaign_div:
            campaign_url = div.a.get('href').strip()
            c_total = div.find('a', 'amt').string.split(" ")
            campaign_total = int(re.sub('[^\d]', '', c_total[0]))
            campaign_donors = int(re.sub('[^\d]', '', c_total[3]))

            ob = GoFundMe.objects.filter(url=campaign_url)
            v = ob.values()
            if (ob.exists() and (int(v[0]['total']) != campaign_total or int(v[0]['donors_number']) != campaign_donors)):
                g = GoFundMe.objects.get(url=campaign_url)
                g.total = campaign_total
                g.donors_number = campaign_donors
                g.save()

        soup.decompose()


# Indiegogo crawler to add campaigns to database
def indiegogo_crawler():
    table = 'indiegogo'
    table_ob = Table.objects.get(table=table)

    url = 'https://life.indiegogo.com/campaign_collections/nepal-relief-fundraisers'
    f = urllib2.urlopen(url)
    contents = f.read()
    soup = BeautifulSoup(contents)
    f.close()

    campaigns = soup.find_all('div', re.compile('^i-project-card'))
    soup.decompose()

    for c in campaigns:
        campaign_url = ('https://www.indiegogo.com' + c.a.get('href')).strip().encode('utf-8')
        title = c.find('div', 'i-title').string.strip().encode('utf-8')
        aid_amount = c.find('span', 'currency-medium').span.string
        aid_amount = int(re.sub('[^\d]', '', aid_amount))
        currency = c.find('span', 'currency-medium').em.string

        c_f = urllib2.urlopen(campaign_url)
        c_contents = c_f.read()
        c_soup = BeautifulSoup(c_contents)

        try:
            created_by = c_soup.find('div', 'i-detailsColumn-title').string.strip().encode('utf-8')
        except:
            created_by = c_soup.find('div', 'pc-organizer-name').string.strip().encode('utf-8')

        try:
            location = c_soup.find('a', 'i-byline-location-link').string.strip().encode('utf-8')
        except:
            try:
                location = c_soup.find_all('div', 'i-detailsColumn-title')[1].next_sibling.next_sibling.string.strip().encode('utf-8')
            except:
                location = c_soup.find('span', 'i-glyph-icon-30-location').next_sibling.string.strip().encode('utf-8')

        c_soup.decompose()


        ob = TableData.objects.filter(name=title, url=campaign_url, table=table_ob)
        v = ob.values()

        if (not ob.exists()) or (ob.exists() and int(v[0]['aid_amount']) != aid_amount):
            obj, created = TableData.objects.update_or_create(name=title, url=campaign_url, table=table_ob, \
                defaults={
                    'name': title, \
                    'url': campaign_url, \
                    'aid_amount': aid_amount, \
                    'extra_field_1': created_by, \
                    'extra_field_2': location, \
                    'table': table_ob})


# Update data of already created campaigns
def update_indiegogo_data():
    table = 'indiegogo'
    table_ob = Table.objects.get(table=table)

    url = 'https://life.indiegogo.com/campaign_collections/nepal-relief-fundraisers'
    f = urllib2.urlopen(url)
    contents = f.read()
    soup = BeautifulSoup(contents)
    f.close()

    campaigns = soup.find_all('div', re.compile('^i-project-card'))
    soup.decompose()

    for c in campaigns:
        campaign_url = ('https://www.indiegogo.com' + c.a.get('href')).strip().encode('utf-8')
        title = c.find('div', 'i-title').string.strip().encode('utf-8')
        aid_amount = c.find('span', 'currency-medium').span.string
        aid_amount = int(re.sub('[^\d]', '', aid_amount))
        currency = c.find('span', 'currency-medium').em.string.strip().encode('utf-8')

        ob = TableData.objects.filter(name=title, url=campaign_url, table=table_ob)
        v = ob.values()

        if (ob.exists() and int(v[0]['aid_amount']) != aid_amount):
                data = TableData.objects.get(name=title, url=campaign_url, table=table_ob)
                data.aid_amount = aid_amount
                data.save()


def giveforward_crawler():
    table = 'give forward'
    table_ob = Table.objects.get(table=table)

    for page in range(1, 4):
        url = 'http://www.giveforward.com/organization/Nepal/summary?r=' + str(page)
        f = urllib2.urlopen(url)
        contents = f.read()
        soup = BeautifulSoup(contents)
        f.close()
        
        campaigns = soup.find_all('li', 'givenow-trigger')
        soup.decompose()

        for c in campaigns:
            campaign_url = c.a.get('href').strip().encode('utf-8')

            c_f = urllib2.urlopen(campaign_url)
            c_contents = c_f.read()
            c_soup = BeautifulSoup(c_contents)
            c_f.close()

            title = c_soup.find('div', 'title-link').h1.string.strip().encode('utf-8')
            aid_amount = c_soup.find('span', 'total').string
            aid_amount = int(re.sub('[^\d]', '', aid_amount))
            goal = c_soup.find('span', 't-nowrap').string[3:].strip().encode('utf-8')
            
            c_soup.decompose()

            ob = TableData.objects.filter(name=title, url=campaign_url, table=table_ob)
            v = ob.values()

            if (not ob.exists()) or (ob.exists() and int(v[0]['aid_amount']) != aid_amount):
                obj, created = TableData.objects.update_or_create(name=title, url=campaign_url, table=table_ob, \
                    defaults={
                        'name': title, \
                        'url': campaign_url, \
                        'aid_amount': aid_amount, \
                        'extra_field_1': goal, \
                        'table': table_ob})


# Update data of already created campaigns
def update_giveforward_data():
    table = 'give forward'
    table_ob = Table.objects.get(table=table)

    for page in range(1, 4):
        url = 'http://www.giveforward.com/organization/Nepal/summary?r=' + str(page)
        f = urllib2.urlopen(url)
        contents = f.read()
        soup = BeautifulSoup(contents)
        f.close()
        
        campaigns = soup.find_all('li', 'givenow-trigger')
        soup.decompose()

        for c in campaigns:
            campaign_url = c.a.get('href').strip().encode('utf-8')
            aid_amount = c.find('p', 'money').string.split(' ')[0].strip().encode('utf-8')
            aid_amount = int(re.sub('[^\d]', '', aid_amount))

            ob = TableData.objects.filter(url=campaign_url, table=table_ob)
            v = ob.values()

            if (ob.exists() and int(v[0]['aid_amount']) != aid_amount):
                    data = TableData.objects.get(url=campaign_url, table=table_ob)
                    data.aid_amount = aid_amount
                    data.save()


# This crawler only works on the local machine
def crowdrise_crawler():
    table = 'crowd rise'
    table_ob = Table.objects.get(table=table)

    url = 'file:///Users/jesuscheng/programming/languages/python/crawlers/crowdrise.html'
    f = urllib2.urlopen(url)
    contents = f.read()
    soup = BeautifulSoup(contents)
    f.close()

    campaigns = soup.find('div', id='teams-results').find_all('div', 'content')
    soup.decompose()

    index = 1
    for c in campaigns:
        campaign_url = c.a.get('href').strip().encode('utf-8')
        aid_amount = int(re.sub('[^\d]', '', c.h3.string))

        c_f = urllib2.urlopen(campaign_url)
        c_contents = c_f.read()
        c_soup = BeautifulSoup(c_contents)
        c_f.close()

        try:
            title = c_soup.find('div', 'fundTitle').h3.string.strip().encode('utf-8')
        except:
            title = c_soup.find('span', 'memberTopNameBig').string.strip().encode('utf-8')

        try:
            aid_amount = int(re.sub('[^\d]', '', c_soup.find('div', id='total_raised').h3.string))
        except:
            aid_amount = int(re.sub('[^\d]', '', c_soup.find('div', 'moneyRaised').h3.string))

        c_soup.decompose()
        index += 1

        ob = TableData.objects.filter(url=campaign_url, table=table_ob)
        v = ob.values()

        if (not ob.exists()) or (ob.exists() and int(v[0]['aid_amount']) != aid_amount):
            obj, created = TableData.objects.update_or_create(name=title, url=campaign_url, table=table_ob, \
                defaults={
                    'name': title, \
                    'url': campaign_url, \
                    'aid_amount': aid_amount, \
                    'table': table_ob})
