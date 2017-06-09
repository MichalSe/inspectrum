from gettingstarted.settings import *

DEBUG = False

DATABASES['default'] = dj_database_url.config(conn_max_age=500)
