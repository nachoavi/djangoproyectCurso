#En este archivo defines las vistas de tu aplicación. Las vistas son funciones o clases que manejan las solicitudes HTTP y generan respuestas, como renderizar plantillas HTML o devolver datos en formato JSON.

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Users
# Create your views here.
#Las views nos permitiran crear las vistas que queremos mostrar al cliente, generando una respuesta Http#
#Ejemplo a continuación 

#Mensaje de bienvenida para el home de la pagina
def welcomeMessage(request,username): #el segundo parametro "username" corresponde a la variable especificada en la url
    print(username)
    return HttpResponse("""<h1>Hello %s!</h1>
                        <table>
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
    
                        </table>""" %username) #con el template %s podemos concatenar la variable username al texto
    
def mainPage(request):
    return HttpResponse("Main Page")

def aboutMessage(request): #Contenido una vez se diriga a la pagina about
    return HttpResponse("This is about me")


def numbers(request,number):
    return HttpResponse("<h1>%s</h1>"%number)


def users(request):
    usuarios = list(Users.objects.values())
    return JsonResponse(usuarios,safe=False)

def tasks(request):
    return HttpResponse("Tareas")

