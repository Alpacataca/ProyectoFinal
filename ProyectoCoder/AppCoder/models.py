from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido}"

class Gerente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    mail = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Profesion {self.profesion} - E-mail {self.mail}"
    
class Avatar(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"


