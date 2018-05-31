from django.contrib import admin

# Register your models here.
from apps.libros.models import Autor, Libros


class AdminAutor(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ciudad', 'genero']

class AdminLibro(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'categoria','autor']


admin.site.register(Libros, AdminLibro)
admin.site.register(Autor, AdminAutor)


