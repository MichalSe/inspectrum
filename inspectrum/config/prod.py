from inspectrum.settings import *

DEBUG = False

DATABASES['default'] = dj_database_url.config()
