from django.shortcuts import render

# Create your views here.
def inicio (request):

    return render(request, "libros/index.html")

def crear (request):

    return render(request,"libros/crear.html")

def actualizar (request):

    return render(request,"libros/actualizar.html")