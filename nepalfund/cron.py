#!/usr/bin/env python
import urllib2, sys

# Use this command: /home/ubuntu/cron.py update 
# or /home/ubuntu/cron.py update godfundme
# update all
# update gofundme
# update indiegogo
# update giveforward
# insert gofundme
# insert indiegogo
# insert giveforward 

def update():
    url = "http://127.0.0.1:8000/update/"
    # url = "http://nepalfund.sonwalkar.io/update/"
    f = urllib2.urlopen(url)
    f.close()


def update_table(table):
    if table == 'all':
        update()
        return
    else:
        url = 'http://127.0.0.1:8000/update/' + str(table)
        # url = 'http://nepalfund.sonwalkar.io/update/' + str(table)
    try:
        f = urllib2.urlopen(url)
        f.close()
    except:
        pass


def insert_table(table):
    url = 'http://127.0.0.1:8000/update/insert-' + str(table)
    # url = 'http://nepalfund.sonwalkar.io/update/insert-' + str(table)

    try:
        f = urllib2.urlopen(url)
        f.close()
    except:
        pass


if __name__ == '__main__':
    return
    # try:
    #     if sys.argv[1] == 'update' and len(sys.argv) == 2:
    #         update()
    #     elif sys.argv[1] == 'update':
    #         update_table(sys.argv[2])
    #     elif sys.argv[1] == 'insert' and len(sys.argv) > 2:
    #         insert_table(sys.argv[2])
    # except:
    #     pass