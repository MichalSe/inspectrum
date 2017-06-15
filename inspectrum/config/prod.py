from inspectrum.settings import *

DEBUG = True

DATABASES['default'] = dj_database_url.config()
