"""
WSGI config for attack_portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/cgi-bin/attack/testenv/lib/python3.6/site-packages')
sys.path.append('/var/www/cgi-bin/attack/')
sys.path.append('/var/www/cgi-bin/attack/portal/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attack_portal.settings")

application = get_wsgi_application()
