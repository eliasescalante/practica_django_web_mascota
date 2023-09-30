from django import forms

class MascotaFormulario(forms.Form):
    nombre = forms.CharField()
    tamaño = forms.CharField()
    raza = forms.CharField()

class EntrenadorFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()

class EntrenamientoFormulario(forms.Form):
    curso = forms.CharField()

