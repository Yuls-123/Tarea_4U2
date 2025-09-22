from django.contrib import admin
from .models import EquipoFutbol
# Register your models here.
class EquipoFutbolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'ciudad', 'fundacion', 'estadio', 'entrenador')
    list_filter = ('pais', 'ciudad')
    search_fields = ('nombre', 'pais', 'ciudad', 'estadio')