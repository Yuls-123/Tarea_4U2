# equipos/forms.py

from django import forms
from .models import EquipoFutbol

class EquipoForm(forms.ModelForm):
    class Meta:
        model = EquipoFutbol
        fields = ['nombre', 'pais', 'ciudad', 'fundacion', 'estadio', 
                 'entrenador', 'capacidad_estadio', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'fundacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'estadio': forms.TextInput(attrs={'class': 'form-control'}),
            'entrenador': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_estadio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }# equipos/forms.py

from django import forms
from .models import EquipoFutbol

class EquipoForm(forms.ModelForm):
    class Meta:
        model = EquipoFutbol
        fields = ['nombre', 'pais', 'ciudad', 'fundacion', 'estadio', 
                 'entrenador', 'capacidad_estadio', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'fundacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'estadio': forms.TextInput(attrs={'class': 'form-control'}),
            'entrenador': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_estadio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }