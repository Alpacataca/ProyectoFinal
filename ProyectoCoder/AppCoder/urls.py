from django.urls import path

from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   #basic
    path('inicio', views.inicio, name="Inicio"), 
    path('equipos', views.equipo, name="Equipos"),
    path('gerentes', views.gerentes, name="Gerentes"),
    path('empleados', views.empleados, name="Empleados"),
    path('busquedaEquipo', views.buscar_equipo, name = "BusquedaEquipo"),
    path ('acercademi',views.acercademi, name = "Acercademi"),
#CRUD CURSO
    path('equipo/list', views.EquipoList.as_view(),name = 'equipoList'),
    path(r'^(?P<pk>\d+)$',views.EquipoDetalle.as_view(),name='equipoDetail'),
    path(r'^nuevo$',views.EquipoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.EquipoUpdate.as_view(),name='equipoEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.EquipoDelete.as_view(),name='equipoDelete'),
#CRUD ESTUDIANTE
   path('empleado/list', views.EmpleadoList.as_view(),name = 'empleadoList'),
    path(r'empleado/^(?P<pk>\d+)$',views.EmpleadoDetalle.as_view(),name='empleadoDetail'),
    path(r'empleado/^nuevo$',views.EmpleadoCreacion.as_view(),name='New'),
    path(r'empleado/^editar/(?P<pk>\d+)$',views.EmpleadoUpdate.as_view(),name='empleadoEdit'),
    path(r'empleado/^borrar/(?P<pk>\d+)$',views.EmpleadoDelete.as_view(),name='empleadoDelete'),
#CRUD PROFESORES
    path('gerente/list', views.GerenteList.as_view(),name = 'gerenteList'),
    path(r'gerente/detail/^(?P<pk>\d+)$',views.GerenteDetalle.as_view(),name='gerenteDetail'),
    path(r'gerente/^nuevo$',views.GerenteCreacion.as_view(),name='New'),
    path(r'gerente/^editar/(?P<pk>\d+)$',views.GerenteUpdate.as_view(),name='gerenteEdit'),
    path(r'gerente/^borrar/(?P<pk>\d+)$',views.GerenteDelete.as_view(),name='gerenteDelete'),
    #login, logout, register y useredit
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar',views.agregarAvatar,name = "AgregarAvatar")
    

]

