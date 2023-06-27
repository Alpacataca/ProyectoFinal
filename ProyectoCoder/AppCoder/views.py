from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def curso(request):
    return render(request,'AppCoder/cursos.html')

def profesores(request):
    return render(request,'AppCoder/profesores.html')

def estudiantes(request):
    return render(request,'AppCoder/estudiantes.html')

   
from AppCoder.forms import CursoFormulario,ProfesoresFormulario,EstudiantesFormulario,BuscaCursoForm
 
from AppCoder.models import Curso,Profesor,Estudiante
 
def cursos(request):
 
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


def profesores(request):
 
      if request.method == "POST":
            miFormulario = ProfesoresFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], profesion=informacion["profesion"], mail = informacion["mail"])
                  profesor.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = ProfesoresFormulario()
 
      return render(request, "AppCoder/profesores.html", {"miFormulario": miFormulario})

def estudiantes(request):
 
      if request.method == "POST":
            miFormulario = EstudiantesFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'])
                  estudiante.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EstudiantesFormulario()
 
      return render(request, "AppCoder/estudiantes.html", {"miFormulario": miFormulario})


def busquedacamada(request):
      return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
      if request.GET:
            camada = request.GET['camada']
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/resultadosPorBusqueda.html",{"cursos":cursos, "camada":camada})
      else:
            respuesta = "No se asignaron datos a la casilla"

      return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})

def buscar_curso(request):
      if request.method=="POST":
            busca_curso = BuscaCursoForm(request.POST)
            
            if busca_curso.is_valid():
                  info = busca_curso.cleaned_data
                  cursos = Curso.objects.filter(nombre=info['curso'])
                  return render(request,"AppCoder/lista.html",{"cursos":cursos})
      else:
            busca_curso = BuscaCursoForm()
            return render(request,"AppCoder/buscar_curso.html", {"miFormulario": busca_curso})

def leerProfesores(request):

      profesores = Profesor.objects.all() 

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



class CursoList(ListView):
      model = Curso
      template_name = "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
      model = Curso
      template_name ="AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
      model = Curso
      success_url = reverse_lazy("/AppCoder/curso/list")
      fields = ['nombre','camada']

class CursoUpdate(UpdateView):
      model = Curso
      success_url = reverse_lazy("/AppCoder/curso/list")
      fields = ['nombre','camada']

class CursoDelete(DeleteView):
      model= Curso
      success_url=reverse_lazy("/AppCoder/curso/list")



class EstudianteList(ListView):
      model = Estudiante
      template_name = "AppCoder/estudiante_list.html"

class EstudianteDetalle(DetailView):
      model = Estudiante
      template_name ="AppCoder/estudiante_detalle.html"

class EstudianteCreacion(CreateView):
      model = Estudiante
      success_url = reverse_lazy("estudianteList")
      fields = ['nombre','apellido']

class EstudianteUpdate(UpdateView):
      model = Estudiante
      success_url = reverse_lazy("estudianteList")
      fields = ['nombre','apellido']

class EstudianteDelete(DeleteView):
      model= Estudiante
      success_url=reverse_lazy("estudianteList")

class ProfesorList(ListView):
      model = Profesor
      template_name = "AppCoder/profesor_list.html"

class ProfesorDetalle(DetailView):
      model = Profesor
      template_name ="AppCoder/profesor_detalle.html"

class ProfesorCreacion(CreateView):
      model = Profesor
      success_url = reverse_lazy("profesorList")
      fields = ['nombre','apellido','profesion','mail']

class ProfesorUpdate(UpdateView):
      model = Profesor
      success_url = reverse_lazy("profesorList")
      fields = ['nombre','apellido','profesion','mail']

class ProfesorDelete(DeleteView):
      model= Profesor
      success_url=reverse_lazy("profesorList")

def login_request(request):
      if request.method =="POST":
            form = AuthenticationForm(request,data = request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario, password = contra)


                  if user is not None:
                        login(request,user)
                        return render (request, "AppCoder/inicio.html",{"mensaje":f"Bienvenido{usuario}"})
                  else:
                        return render (request, "AppCoder/inicio.html", {"mensaje": "Error, datos incorrectos"})
            else: 
                  return render(request,"AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})
            
      form = AuthenticationForm()
      return render (request, "AppCoder/login.html",{'form':form})

def register(request):
      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render (request, "AppCoder/inicio.html" , {"mensaje":"Usuario Creado:)"})
      
      else:
            form = UserCreationForm()
      
      return render(request,"AppCoder/registro.html", {"form":form})

