from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import EquipoFutbol
from .forms import EquipoForm

# Create your views here.
def home(request):
    equipos = EquipoFutbol.objects.all()
    return render(request, 'home.html', {'equipos': equipos})

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.usuario = request.user
            equipo.save()
            return redirect('home')
    else:
        form = EquipoForm()
    return render(request, 'equipos/crear_equipo.html', {'form': form})

@login_required
def editar_equipo(request, id):
    equipo = get_object_or_404(EquipoFutbol, pk=id, usuario=request.user)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'equipos/editar_equipo.html', {'form': form, 'equipo': equipo})

@login_required
def eliminar_equipo(request, id):
    equipo = get_object_or_404(EquipoFutbol, pk=id, usuario=request.user)
    if request.method == 'POST':
        equipo.delete()
        return redirect('home')
    return render(request, 'equipos/eliminar_equipo.html', {'equipo': equipo})