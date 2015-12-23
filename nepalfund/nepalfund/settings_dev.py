# Development settings in my local machine

from settings import *

DEBUG = TEMPLATE_DEBUG = True

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'nepalfund',
#        'USER': 'root',
#        'PASSWORD': 'root',
#        'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',
#        'PORT': '3306',
#        'ENCODING': 'utf-8',
#    }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nepalfund',
        'USER': 'root',
        'PASSWORD': 'heisenberg',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'ENCODING': 'utf-8',
    }
}
