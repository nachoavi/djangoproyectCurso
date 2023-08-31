#En este archivo defines las vistas de tu aplicación. Las vistas son funciones o clases que manejan las solicitudes HTTP y generan respuestas, como renderizar plantillas HTML o devolver datos en formato JSON.

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Users,Task
from django.shortcuts import get_object_or_404,get_list_or_404,render #Estas funciones nos permiten traer el error 404 en caso de no encontrar listas o objetos y asi evitar que se caiga el servidor
#Si importamos render podremos mostrar archivos html como templates en nuetras views


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
    return render(request,"index.html")

def aboutMessage(request): #Contenido una vez se diriga a la pagina about
    title = "Estamos aprendiendo Django"
    username = "Naxo"
    return render(request,"about.html",{'titulo':title,'username':username})


def numbers(request,number):
    return HttpResponse("<h1>%s</h1>"%number)


def users(request):
    #usuarios = list(Users.objects.values())
    usuarios = Users.objects.all()
    #return JsonResponse(usuarios,safe=False)
    return render(request,"usersTable.html",{
        'usuarios':usuarios
    })

#Encontrar tarea por id
def tasks(request,task_id):
    #tareaEspecifica = Task.objects.get(id=task_id) asi se haria sin gestion de errores
    tareaEspecifica = get_object_or_404(Task, id=task_id) #Asi se hace gestionando el error y redirigiendo a un 404 en caso de no encontrar el objeto
    return HttpResponse("Tarea: %s" %tareaEspecifica.title)

#Encontrar tarea por nombre
def findTaskbyName(request, task_name):
    tareaEspecificaByName = get_object_or_404(Task,title=task_name)
    return HttpResponse("La tarea por nombre es: %s" %tareaEspecificaByName.title)

