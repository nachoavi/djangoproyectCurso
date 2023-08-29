# Al igual que wsgi.py, este archivo es utilizado para implementar el proyecto, pero utilizando ASGI (Asynchronous Server Gateway Interface). Es necesario si deseas ejecutar aplicaciones asincrónicas en Django.
"""
ASGI config for cursoFazt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cursoFazt.settings')

application = get_asgi_application()
