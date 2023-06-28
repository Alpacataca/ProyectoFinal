from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    mail = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Profesion {self.profesion} - E-mail {self.mail}"

    