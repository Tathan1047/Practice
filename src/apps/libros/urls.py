from django.conf.urls import url

from apps.libros import views
from apps.libros.views import crear, inicio, listar, InicioTemplateView, CrearLibroCreateView, \
    EditarLibroUpdateView, ListarLibrosListView,EliminarLibroDeleteView, ListarCategoriasListView, \
    EditarCategoriaUpdateView

urlpatterns = [
    # url(r'^$', inicio,name="inicio"),
    # url(r'^crear/$', views.crear, name="crear"),
    # url(r'^crear_categoria/$', views.crear_categoria, name="crear_categoria"),
    # url(r'^listar/$', views.listar, name="listar"),
    # url(r'^listarc/$', views.listarc, name="listarc"),
    # url(r'^editarlibro/(?P<pk>\d+)/$', views.editarlibro, name="editarlibro"),
    # url(r'^eliminarlibro/(?P<pk>\d+)/$', views.eliminarlibro, name="eliminarlibro"),
    # url(r'^actualizar/', actualizar, name="actualizar"),


    url(r'^$', InicioTemplateView.as_view(),name="inicio"),
    url(r'^crear/$', CrearLibroCreateView.as_view(), name="crear"),
    url(r'^listar/$', ListarLibrosListView.as_view(), name="listar"),
    url(r'^editarlibro/(?P<pk>\d+)/$', EditarLibroUpdateView.as_view(), name="editarlibro"),
    url(r'^eliminarlibro/(?P<pk>\d+)/$', EliminarLibroDeleteView.as_view(), name="eliminarlibro"),

    url(r'^listarc/$', ListarCategoriasListView.as_view(), name="listarc"),
    url(r'^crear_categoria/$', views.crear_categoria, name="crear_categoria"),
    url(r'^editarcategoria/(?P<pk>\d+)/$', EditarCategoriaUpdateView.as_view(), name="editarcategoria"),
]
