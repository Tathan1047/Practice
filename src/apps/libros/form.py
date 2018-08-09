from django import forms
from apps.libros.models import Libros, Categoria


class crearform(forms.ModelForm):
    class Meta:
        model = Libros

        fields =[
            'autor',
            'titulo',
            'categoria',
            'editorial',
        ]

        labels = {
            'autor': 'Autor',
            'titulo': 'Nombre',
            'categoria':'Categoria',
            'editorial':'Editorial'
        }

        widgets = {
            'autor': forms.Select(attrs={'class':'form-control' }),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de obra'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'editorial': forms.Select(attrs={'class': 'form-control'}),
        }



class crearcategoria (forms.ModelForm):
    class Meta:
        model = Categoria

        fields =[
            'categoria',
        ]

        labels = {
            'categoria': '',
        }

        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria de Libros'}),

        }


