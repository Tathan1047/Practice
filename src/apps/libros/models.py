from django.db import models


class Autor (models.Model):

    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)


    def __str__(self):
       return self.nombre

class Categoria (models.Model):
    categoria = models.CharField(max_length=50)


    def __str__(self):
        return self.categoria


class Editoriales(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libros (models.Model):
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    titulo=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editoriales, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



