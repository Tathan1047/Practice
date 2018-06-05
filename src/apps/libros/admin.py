from django.contrib import admin

# Register your models here.
from apps.libros.models import Autor, Libros, Categoria


class AdminAutor(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ciudad', 'genero']

class AdminLibro(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'categoria','autor']

class AdminCategoria(admin.ModelAdmin):
    list_display = ('id', 'nombre',)


admin.site.register(Libros, AdminLibro)
admin.site.register(Autor, AdminAutor)
admin.site.register(Categoria, AdminCategoria)



