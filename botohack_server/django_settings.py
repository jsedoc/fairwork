from botohack_server.settings import *
import django_heroku
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', 'mechanicaljerk.herokuapp.com']

TIME_ZONE = 'America/Los_Angeles'

DATABASES['default'] =  dj_database_url.config()

django_heroku.settings(locals())

print("Django specific settings loaded.")
print("Access key: %s" % AWS_ACCESS_KEY_ID)
print("Debug: %s" % DEBUG)