# Este archivo es utilizado para implementar el proyecto en servidores web compatibles con la interfaz WSGI (Web Server Gateway Interface). Ayuda a servir la aplicación Django utilizando servidores web como Apache o Nginx.

"""
WSGI config for cursoFazt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cursoFazt.settings')

application = get_wsgi_application()
