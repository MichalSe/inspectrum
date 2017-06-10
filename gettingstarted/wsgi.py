"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

import os, sys
# add the hellodjango project path into the sys.path
#sys.path.append('<PATH_TO_MY_DJANGO_PROJECT>/hellodjango')

# add the virtualenv site-packages path to the sys.path
#sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inspectrum-server.settings.prod")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
