from django.urls import path
from MascotaApp import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('mascotaFormulario', views.mascotaFormulario, name = "Mascota"),
    path('entrenadorFormulario', views.entrenadorFormulario, name = "Entrenador"),
    path('entrenamientoFormulario', views.entrenamientoFormulario, name = "Entrenamiento"),
]