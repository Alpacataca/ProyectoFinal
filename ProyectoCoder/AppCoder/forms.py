from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    profesion = forms.CharField()
    mail = forms.CharField()

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()


class BuscaCursoForm(forms.Form):
    curso = forms.CharField()
    