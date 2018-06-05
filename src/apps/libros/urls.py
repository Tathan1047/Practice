from django.conf.urls import url

from apps.libros import views
from apps.libros.views import crear, inicio, actualizar,listar

app_name = "libros"
urlpatterns = [
    url(r'inicio/$', inicio,name="inicio"),
    url(r'^crear/$', views.crear, name="crear"),
    url(r'^listar/$', views.listar, name="listar"),
    url(r'^listarc/$', views.listarc, name="listarc"),
    url(r'^editarlibro/(?P<pk>\d+)/$', views.editarlibro, name="editarlibro"),
    url(r'actualizar/', actualizar, name="actualizar"),


]
