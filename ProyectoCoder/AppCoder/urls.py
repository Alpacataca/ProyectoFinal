from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('inicio', views.inicio, name="Inicio"), 
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('busquedaCurso', views.buscar_curso, name = "BusquedaCurso"),
    path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
#CRUD CURSO
    path('curso/list', views.CursoList.as_view(),name = 'cursoList'),
    path(r'^(?P<pk>\d+)$',views.CursoDetalle.as_view(),name='cursoDetail'),
    path(r'^nuevo$',views.CursoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.CursoUpdate.as_view(),name='cursoEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.CursoDelete.as_view(),name='cursoDelete'),
#CRUD ESTUDIANTE
    path('estudiante/list', views.EstudianteList.as_view(),name = 'estudianteList'),
    path(r'^(?P<pk>\d+)$',views.EstudianteDetalle.as_view(),name='estudianteDetail'),
    path(r'^nuevo$',views.EstudianteCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.EstudianteUpdate.as_view(),name='estudianteEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.EstudianteDelete.as_view(),name='estudianteDelete'),
#CRUD PROFESORES
    path('profesores/list', views.ProfesorList.as_view(),name = 'profesorList'),
    path(r'^(?P<pk>\d+)$',views.ProfesorDetalle.as_view(),name='profesorDetail'),
    path(r'^nuevo$',views.ProfesorCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.ProfesorUpdate.as_view(),name='profesorEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ProfesorDelete.as_view(),name='profesorDelete'),
]

