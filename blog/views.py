from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home_view(request):
    publicaciones = Publicacion.objects.all().order_by("-id")
    return render(request, "home.html", {"publicaciones": publicaciones})

def add_view(request):
    if request.method == "POST":
        Publicacion.objects.create(titulo=request.POST.get("titulo"), cuerpo=request.POST.get("cuerpo"))
        return redirect("/")
    return render(request, "agregar.html", {} )