"""
WSGI config for ana_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/django-tutorial/apps_wsgi')
sys.path.append('/home/django-tutorial/apps_wsgi/adm')
os.environ['PYTHON_EGG_CACHE'] = '/home/django-tutorial/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'adm.settings'
application = get_wsgi_application()
