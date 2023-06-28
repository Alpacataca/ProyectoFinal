from django.urls import path

from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   #basic
    path('inicio', views.inicio, name="Inicio"), 
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('busquedaCurso', views.buscar_curso, name = "BusquedaCurso"),
    path ('acercademi',views.acercademi, name = "Acercademi"),
#CRUD CURSO
    path('curso/list', views.CursoList.as_view(),name = 'cursoList'),
    path(r'^(?P<pk>\d+)$',views.CursoDetalle.as_view(),name='cursoDetail'),
    path(r'^nuevo$',views.CursoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.CursoUpdate.as_view(),name='cursoEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.CursoDelete.as_view(),name='cursoDelete'),
#CRUD ESTUDIANTE
   path('estudiante/list', views.EstudianteList.as_view(),name = 'estudianteList'),
    path(r'estudiante/^(?P<pk>\d+)$',views.EstudianteDetalle.as_view(),name='estudianteDetail'),
    path(r'estudiante/^nuevo$',views.EstudianteCreacion.as_view(),name='New'),
    path(r'estudiante/^editar/(?P<pk>\d+)$',views.EstudianteUpdate.as_view(),name='estudianteEdit'),
    path(r'estudiante/^borrar/(?P<pk>\d+)$',views.EstudianteDelete.as_view(),name='estudianteDelete'),
#CRUD PROFESORES
    path('profesor/list', views.ProfesorList.as_view(),name = 'profesorList'),
    path(r'profesor/detail/^(?P<pk>\d+)$',views.ProfesorDetalle.as_view(),name='profesorDetail'),
    path(r'profesor/^nuevo$',views.ProfesorCreacion.as_view(),name='New'),
    path(r'profesor/^editar/(?P<pk>\d+)$',views.ProfesorUpdate.as_view(),name='profesorEdit'),
    path(r'profesor/^borrar/(?P<pk>\d+)$',views.ProfesorDelete.as_view(),name='profesorDelete'),
    #login, logout, register y useredit
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar',views.agregarAvatar,name = "AgregarAvatar")
    

]

