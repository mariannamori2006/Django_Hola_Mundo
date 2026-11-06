from django.shortcuts import render
from .models import Mensaje

# Create your views here.
def home(request):
    mensajes = Mensaje.objects.all()

    return render(request, 'control/home.html', {'mensajes':mensajes})