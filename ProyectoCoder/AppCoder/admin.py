from django.contrib import admin
from .models import Equipo, Empleado, Gerente,Avatar
# Register your models here.

admin.site.register(Equipo)
admin.site.register(Empleado)
admin.site.register(Gerente)
admin.site.register(Avatar)