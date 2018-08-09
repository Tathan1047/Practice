from django.contrib import admin

# Register your models here.
from apps.libros.models import Autor, Libros, Categoria, Editoriales


class AdminAutor(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ciudad', 'genero']

class AdminLibro(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'categoria','editorial','autor']

class AdminCategoria(admin.ModelAdmin):
    list_display = ('id', 'categoria',)

class AdminEditoriales(admin.ModelAdmin):
    list_display = ('id', 'nombre',)

admin.site.register(Libros, AdminLibro)
admin.site.register(Autor, AdminAutor)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Editoriales, AdminEditoriales)




