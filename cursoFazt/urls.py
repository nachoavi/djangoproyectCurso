#Similar al urls.py en una aplicación, este archivo define las rutas URL para el proyecto. Aquí se especifican los patrones de URL y se asignan a controladores específicos.

"""
URL configuration for cursoFazt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #El include nos servira para incluir urls propias de una APP 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myFirstApp.urls')) #aqui estamos incluyendo las url que vienen de la app que antes creamos, es importante que señalar que si dejamos la ruta vacia, estas tomaran las que vienen de la app, si nosotro colocamos una ruta aqui, las rutas de la app precidiran de esta
]
