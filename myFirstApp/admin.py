from django.contrib import admin
from .models import Users,Task

# Register your models here.
#Aquí se define la configuración de la interfaz de administración de Django para la aplicación. Puedes registrar tus modelos para que sean administrables desde el panel de administración.

admin.site.register(Task)
admin.site.register(Users)