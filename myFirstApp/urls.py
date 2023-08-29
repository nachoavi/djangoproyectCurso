#En este archivo defines las rutas URL para tus vistas. Asocia patrones de URL con funciones de vista o clases para determinar cómo se manejarán las solicitudes entrantes.

#El sentido de crear un arhivo para las urls en la aplicación es que se definan aqui y no en la carpeta principal, si no tendriamos demasiadas por cada app
from django.urls import path #Nuestro archivo urls se le debe importar el path y las vistas o views de nuestra app
from . import views

urlpatterns = [
    path('',views.mainPage), 
    path('about/',views.aboutMessage),
    path('welcome/<str:username>',views.welcomeMessage),#Podemos recibir datos de la url y usarlos como parametros o params, esto colocando una variable entre <tipoDato:variable>, esta variable podra ser extraida por la función views.welcomeMessage para ser utilizada.
    path('number/<int:number>',views.numbers),
    path('users/',views.users),
    path('tasks/<int:task_id>',views.tasks),
    path('tasksByName/<str:task_name>',views.findTaskbyName)
] 