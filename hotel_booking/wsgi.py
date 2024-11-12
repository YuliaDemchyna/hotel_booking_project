"""
WSGI config for hotel_booking project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

project_home = '/home/yuliademchyna/hotel_booking_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hotel_booking.settings'

activate_env = os.path.expanduser('/home/yuliademchyna/hotel_booking_project/myenv/bin/activate_this.py')
with open(activate_env) as f:
    exec(f.read(), {'__file__': activate_env})

application = get_wsgi_application()

