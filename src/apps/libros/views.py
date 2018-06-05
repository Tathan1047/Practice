from django.shortcuts import render, redirect

from apps.libros.form import crearform
from .models import Libros, Categoria


# Create your views here.
def inicio (request):

    return render(request, "libros/index.html")

def crear (request):
    form = crearform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('libros:listar')
    contexto = {'form': form}
    return render(request, 'libros/crear.html', contexto)

def actualizar (request):

    return render(request,"libros/actualizar.html")

def listar (request):
    libros=Libros.objects.all()
    data={'libros':libros}
    return render(request,"libros/list_book.html",context=data)

def listarc (request):
    cat=Categoria.objects.all()
    data={'categorias':cat}
    return render(request,"libros/list_categoria.html",context=data)

def editarlibro(request,pk):
    instancia = Libros.objects.get(id=pk)
    if request.method == 'POST':
        form = crearform(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('libros:listar')
    else:
        form = crearform(instance=instancia)

    contexto = {'form': form}
    return render(request, 'libros/editarlibro.html', contexto)