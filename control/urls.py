from django.urls import path 
from .import views 

#URL de la aplicacion
urlpatterns = [
    path("", views.home, name="home"),
]