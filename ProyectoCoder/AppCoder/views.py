from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppCoder.forms import EquipoFormulario,GerenteFormulario,EmpleadosFormulario,BuscaEquipoForm,UserRegisterForm,UserEditForm,AvatarFormulario
from AppCoder.models import Equipo,Gerente,Empleado,Avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request,"AppCoder/inicio.html")
@login_required
def equipo(request):
    return render(request,'AppCoder/equipo.html')
@login_required
def gerentes(request):
    return render(request,'AppCoder/gerente.html')
@login_required
def empleados(request):
    return render(request,'AppCoder/empleados.html')
@login_required
def acercademi(request):
      return render(request,'AppCoder/acercademi.html')
@login_required
def equipo(request):
 
      if request.method == "POST":
            miFormulario = EquipoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  equipo = Equipo(nombre=informacion['nombre'], camada=informacion['camada'])
                  equipo.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EquipoFormulario()
 
      return render(request, "AppCoder/equipo.html", {"miFormulario": miFormulario})

@login_required
def gerentes(request):
 
      if request.method == "POST":
            miFormulario = GerenteFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  gerente = Gerente(nombre=informacion["nombre"], apellido=informacion["apellido"], profesion=informacion["profesion"], mail = informacion["mail"])
                  gerente.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = GerenteFormulario()
 
      return render(request, "AppCoder/gerente.html", {"miFormulario": miFormulario})
@login_required
def empleados(request):
 
      if request.method == "POST":
            miFormulario = EmpleadosFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  empleado = Empleado(nombre=informacion['nombre'], apellido=informacion['apellido'])
                  empleado.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = EmpleadosFormulario()
 
      return render(request, "AppCoder/empleado.html", {"miFormulario": miFormulario})

@login_required
def busquedaequipo(request):
      return render(request, "AppCoder/busquedaEquipo.html")
@login_required
def buscar(request):
      if request.GET:
            camada = request.GET['nombre']
            equipo = Equipo.objects.filter(nombre__icontains=equipo)

            return render(request, "AppCoder/resultadosPorBusqueda.html",{"nombre":equipo, "camada":camada})
      else:
            respuesta = "No se asignaron datos a la casilla"

      return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})
@login_required
def buscar_equipo(request):
      if request.method=="POST":
            busca_equipo = BuscaEquipoForm(request.POST)
            
            if busca_equipo.is_valid():
                  info = busca_equipo.cleaned_data
                  equipos = Equipo.objects.filter(nombre=info['equipo'])
                  return render(request,"AppCoder/lista.html",{"equipos":equipos})
      else:
            busca_equipo = BuscaEquipoForm()
            return render(request,"AppCoder/buscar_equipo.html", {"miFormulario": busca_equipo})



class EquipoList(ListView):
      model = Equipo
      template_name = "AppCoder/equipo_list.html"

class EquipoDetalle(DetailView):
      model = Equipo
      template_name ="AppCoder/equipo_detalle.html"

class EquipoCreacion(CreateView):
      model = Equipo
      success_url = reverse_lazy("equipoList")
      fields = ['nombre','camada']

class EquipoUpdate(UpdateView):
      model = Equipo
      success_url = reverse_lazy("equipoList")
      fields = ['nombre','camada']

class EquipoDelete(DeleteView):
      model= Equipo
      success_url=reverse_lazy("equipoList")



class EmpleadoList(ListView):
      model = Empleado
      template_name = "AppCoder/empleado_list.html"

class EmpleadoDetalle(DetailView):
      model = Empleado
      template_name ="AppCoder/empleado_detalle.html"

class EmpleadoCreacion(CreateView):
      model = Empleado
      success_url = reverse_lazy("empleadoList")
      fields = ['nombre','apellido']

class EmpleadoUpdate(UpdateView):
      model = Empleado
      success_url = reverse_lazy("empleadoList")
      fields = ['nombre','apellido']

class EmpleadoDelete(DeleteView):
      model= Empleado
      success_url=reverse_lazy("empleadoList")



class GerenteList(ListView):
      model = Gerente
      template_name = "AppCoder/gerente_list.html"

class GerenteDetalle(DetailView):
      model = Gerente
      template_name ="AppCoder/gerente_detalle.html"

class GerenteCreacion(CreateView):
      model = Gerente
      success_url = reverse_lazy("gerenteList")
      fields = ['nombre','apellido','profesion','mail']

class GerenteUpdate(UpdateView):
      model = Gerente
      success_url = reverse_lazy("gerenteList")
      fields = ['nombre','apellido','profesion','mail']

class GerenteDelete(DeleteView):
      model= Gerente
      success_url=reverse_lazy("gerenteList")

def login_request(request):

      if request.method =="POST":

            form = AuthenticationForm(request,data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario, password = contra)


                  if user is not None:
                        login(request,user)

                        return render (request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )
                  else:

                        return render (request, "AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )
                  
            else: 

                        return render(request,"AppCoder/inicio.html" , {"mensaje":"Error, formulario erroneo"})
            
      form = AuthenticationForm()
      return render(request, "AppCoder/login.html", {'form':form} )

def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)

            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render (request, "AppCoder/inicio.html" , {"mensaje":"Usuario Creado :)"})
      
      else:
            form = UserRegisterForm()
      
      return render(request,"AppCoder/registro.html" , {"form":form})



@login_required
def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppCoder/padre.html",{"url":avatares[0].imagen.url})

@login_required
def editarPerfil(request):
      usuario = request.user

      if request.method =="POST":
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data

                  usuario.email = informacion ['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = UserEditForm(initial = { 'email':usuario.email})
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            avatar_anterior = Avatar.objects.filter(user=request.user)
            if (len(avatar_anterior) > 0):
                avatar_anterior.delete()
            # avatar_nuevo = Avatar(user = request.user, imagen = form.cleaned_data["imagen"])
            # avatar_nuevo.save()
            u = User.objects.get(username=request.user)
            avatar_nuevo = Avatar(
                user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar_nuevo.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AvatarFormulario()
    return render(request, "AppCoder/agregarAvatar.html", {"miFormulario": miFormulario})






