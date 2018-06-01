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


class Libros (models.Model):
    autor=models.ForeignKey(Autor)
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria)

    def __str__(self):
        return self.nombre


