from django.db import models

# Create your models here.
#En este archivo defines tus modelos, que son las representaciones de las tablas en la base de datos. Utilizas clases de Python para definir la estructura de los datos y las relaciones entre ellos.


class Users(models.Model):
    username = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=200)
    
    
class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
     #El valor models.CASCADE de on_delete indica que cuando el objeto relacionado (referenciado) se elimine, se eliminarán automáticamente también los objetos que dependen de él. 