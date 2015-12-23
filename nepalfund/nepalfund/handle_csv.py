import re, csv
from django.http import HttpResponse
from fundraising.models import *

def download_csv(model):
    response = HttpResponse(content_type='text/csv')
    table_name = re.sub('\s+', '_', str(model.table)).lower()
    attachment = 'attachment; filename=' + table_name + '.csv'
    response['Content-Disposition'] = attachment

    header = Table.objects.get(table=model)

    fields = ['name', 'url', 'aid_amount', 'extra_field_1', 'extra_field_2', 'extra_field_3', 
        'extra_field_4', 'extra_field_5', 'extra_field_6', 'extra_field_7']

    # List of fields that are enable
    enabled_headers = []

    for f in fields:
        if getattr(header, f) != None and getattr(header, f) != False and getattr(header, f) != '' and getattr(header, f) != ' ':
            enabled_headers.append(f)

    data = TableData.objects.filter(table=model)

    writer = csv.writer(response)
    writer.writerow(enabled_headers)

    for row in data:
        dat = []
        for h in enabled_headers:
            try:
                # Have to check if it is a string or decimal first because you cannot encode decimal
                if h != 'aid_amount':
                    fi = getattr(row, h).encode('utf-8')
                else:
                    fi = getattr(row, h)

                dat.append(fi)
            except:
                pass

        writer.writerow(dat)

    return response


def handle_csv_gofundme(f):
    file = f
    data = [row for row in csv.reader(file.read().splitlines())]
    rownum = 0

    for row in data:
        if rownum != 0:
            ob = GoFundMe.objects.filter(campaign=row[1])
            v = ob.values()
            if (not ob.exists()) or (ob.exists() and int(v[0]['donors_number']) != int(row[5])):
                go = int(re.sub('[^\d^\.]', '', row[3]))
                tot = int(re.sub('[^\d^\.]', '', row[4]))
                obj, created = GoFundMe.objects.update_or_create(campaign=row[1], \
                    defaults={'url': row[0], \
                    'campaign': row[1], \
                    'location': row[2], \
                    'goal': go, \
                    'total': tot, \
                    'donors_number': int(row[5]), \
                    'created_by': row[6], \
                    'date_created': row[7], \
                    'date_closed': row[8]})

        rownum += 1


# Handle CSV uploads for generic tables
def handle_csv(f, model):
    file = f
    data = [row for row in csv.reader(file.read().splitlines())]

    header = Table.objects.get(table=model)

    # This is the index of the fields in the CSV file
    fields = {
        'name': 0,
        'url': 1,
        'aid_amount': 2,
        'extra_field_1': 3,
        'extra_field_2': 4,
        'extra_field_3': 5,
        'extra_field_4': 6,
        'extra_field_5': 7,
        'extra_field_6': 8,
        'extra_field_7': 9
    }

    size = len(fields)
    index = range(0, size)

    # This will handle when there are fields that are disable
    for key, value in fields.items():
        if getattr(header, key) == None or getattr(header, key) == False or getattr(header, key) == '' or getattr(header, key) == ' ':
            index[value] = 50
            for i in range(value+1, size):
                index[i] -= 1

    rownum = 0
    row_values = [''] * size
    for row in data:
        if rownum != 0:
            for i in range(0, size):
                if i != 2:
                    try:
                        row_values[i] = row[index[i]]
                    except:
                        row_values[i] = ''
                else:
                    try:
                        if type(row[index[i]]) == str:
                            row_values[i] = float(re.sub('[^\d^\.]', '', row[index[i]]))
                        else:
                            row_values[i] = float(row[index[i]])
                    except:
                        row_values[i] = 0

            ob = TableData.objects.filter(name=row_values[0], url=row_values[1], table=model)
            v = ob.values()

            if (not ob.exists()) or (ob.exists() and int(v[0]['aid_amount']) != row_values[2]):
                obj, created = TableData.objects.update_or_create(name=row_values[0],  url=row_values[1], table=model, \
                    defaults={'name': row_values[0], \
                        'url': row_values[1], \
                        'aid_amount': row_values[2], \
                        'extra_field_1': row_values[3], \
                        'extra_field_2': row_values[4], \
                        'extra_field_3': row_values[5], \
                        'extra_field_4': row_values[6], \
                        'extra_field_5': row_values[7], \
                        'extra_field_6': row_values[8], \
                        'extra_field_7': row_values[9], \
                        'table': model})
        rownum += 1    


# This handles the CSV with the right format with empty columns where there is no field. Old
def handle_formatted_csv_upload(f, model):
    file = f
    data = [row for row in csv.reader(file.read().splitlines())]
    rownum = 0
    
    for row in data:
        if rownum != 0:
            try:
                name = row[0]
            except:
                name = ''

            try:
                url = row[1]
            except:
                url = ''

            try:
                tot = int(re.sub('[^\d^\.]', '', row[2]))
                aid_amount = tot
            except:
                aid_amount = 0

            try:
                extra_field_1 = row[3]
            except:
                extra_field_1 = ''

            try:
                extra_field_2 = row[4]
            except:
                extra_field_2 = ''

            try:
                extra_field_3 = row[5]
            except:
                extra_field_3 = ''

            try:
                extra_field_4 = row[6]
            except:
                extra_field_4 = ''

            try:
                extra_field_5 = row[7]
            except:
                extra_field_5 = ''

            ob = TableData.objects.filter(name=row[0], table=model)
            v = ob.values()

            if (not ob.exists()) or (ob.exists() and int(v[0]['aid_amount']) != aid_amount):
                obj, created = TableData.objects.update_or_create(name=name, table=model, \
                    defaults={'name': name, \
                        'url': url, \
                        'aid_amount': aid_amount, \
                        'extra_field_1': extra_field_1, \
                        'extra_field_2': extra_field_2, \
                        'extra_field_3': extra_field_3, \
                        'extra_field_4': extra_field_4, \
                        'extra_field_5': extra_field_5, \
                        'table': model})
        rownum += 1


# def handle_csv_corporate(f):
#     file = f
#     data = [row for row in csv.reader(file.read().splitlines())]
#     rownum = 0

#     for row in data:
#         if rownum != 0:
#             ob = Corporate.objects.filter(organization=row[1])
#             v = ob.values()
#             tot = int(re.sub('[^\d^\.]', '', row[2]))
#             if (not ob.exists()) or (ob.exists() and int(v[0]['aid_amount']) != tot):
#                 obj, created = Corporate.objects.update_or_create(organization=row[1], \
#                     defaults={'organization': row[1], \
#                     'aid_amount': tot})
#         rownum += 1