from django.apps import AppConfig
# Este archivo contiene la configuración de la aplicación. Puedes personalizar el comportamiento de la aplicación, como su nombre legible por humanos.

class MyfirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myFirstApp'
