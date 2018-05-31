from django.conf.urls import url

from apps.libros import views

urlpatterns = [
    url(r'^inicio/', views.inicio,name="inicio"),

]
