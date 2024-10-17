"""
WSGI config for docappsystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Ensure this points to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.docappsystem.settings')  # Adjusted to reflect the path

application = get_wsgi_application()
