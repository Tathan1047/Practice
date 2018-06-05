from django import forms

from apps.libros.models import Libros


class crearform(forms.ModelForm):
    class Meta:
        model = Libros

        fields =[
            'autor',
            'nombre',
            'categoria',
        ]

        labels = {
            'autor': 'Autor',
            'nombre': 'Nombre',
            'categoria':'Categoria',
        }

        widgets = {
            'autor': forms.Select(attrs={'class':'form-control', }),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de obra'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
        }





