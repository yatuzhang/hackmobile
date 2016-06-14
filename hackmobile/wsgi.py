"""
WSGI config for hackmobile project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

ppath = '/home/yatu/hackmobile_server/hackmobile'

sys.path.append(ppath)
os.environ.setdefault("PYTHONPATH", ppath)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackmobile.settings")

application = get_wsgi_application()
