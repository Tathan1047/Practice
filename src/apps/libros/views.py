from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from apps.libros.form import crearform, crearcategoria
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


def listar (request):
    libros=Libros.objects.all()
    data={'libros':libros}
    return render(request,"libros/list_book.html",context=data)

#----- Listar Regitros Categoria ---------#
def listarc (request):
    cat=Categoria.objects.all()
    data={'categorias':cat}
    return render(request,"libros/list_categoria.html",context=data)
#----- Fin Listar Regitros Categoria ---------#


#----- Editar Regitros de Libro ---------#

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

#----- Fin Editar Regitros de Libro ---------#


#----Función Crear Categoria --------------#
def crear_categoria (request):
    form = crearcategoria(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('libros:listarc')
    contexto = {'form': form}
    return render(request, 'libros/crear_categoria.html', contexto)
#----Fin  Función Crear Categoria --------------#



# ------- Funcion para eliminar ------------#
def eliminarlibro(request,pk):
    instancia = Libros.objects.get(id=pk)
    instancia.delete()
    return redirect('libros:listar')
    return render(request, 'libros/eliminar.html',)
# -------Fin  Funcion para eliminar -------#


# =====================USING CLASS BASE VIEW MODULE BOOKS =========================== #
class InicioTemplateView(TemplateView):
    template_name = 'libros/index.html'

class ListarLibrosListView(ListView):
    queryset = Libros.objects.all()
    template_name = 'libros/list_book.html'

class CrearLibroCreateView(CreateView):
    template_name = 'libros/crear.html'
    model = Libros
    form_class = crearform
    success_url = reverse_lazy('libros:listar')

class EditarLibroUpdateView(UpdateView):
    model = Libros
    template_name = 'libros/editarlibro.html'
    form_class = crearform
    success_url = reverse_lazy('libros:listar')

class EliminarLibroDeleteView(DeleteView):
    model = Libros
    template_name = 'libros/eliminar.html'
    success_url = reverse_lazy('libros:listar')

# =====================END CLASS BASE VIEW MODULE BOOKS =========================== #

# =====================USING CLASS BASE VIEW MODULE CATEGORIES=========================== #

class ListarCategoriasListView(ListView):
    queryset = Categoria.objects.all()
    template_name = 'libros/list_categoria.html'

class EditarCategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'libros/crear_categoria.html'
    form_class = crearcategoria
    success_url = reverse_lazy('libros:listarc')

class EliminarCategoriaView(DeleteView):
    model = Categoria
    template_name = ''





