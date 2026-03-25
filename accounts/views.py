from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Usuario, Ciudad
from .forms import UsuarioForm, CiudadForm


def es_admin(user):
    return user.is_authenticated and (user.is_superuser or user.rol == "admin")


@login_required
def home(request):
    context = {
        "total_usuarios": Usuario.objects.count(),
        "total_ciudades": Ciudad.objects.count(),
        "es_admin": es_admin(request.user),
    }
    return render(request, "home.html", context)


@login_required
@user_passes_test(es_admin)
def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_usuarios")
    else:
        form = UsuarioForm()

    return render(request, "usuarios/crear_usuario.html", {"form": form})


@login_required
@user_passes_test(es_admin)
def lista_usuarios(request):
    usuarios = Usuario.objects.all().select_related("ciudad")
    return render(request, "usuarios/lista_usuarios.html", {"usuarios": usuarios})


@login_required
@user_passes_test(es_admin)
def crear_ciudad(request):
    if request.method == "POST":
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_ciudades")
    else:
        form = CiudadForm()

    return render(request, "ciudades/crear_ciudad.html", {"form": form})


@login_required
@user_passes_test(es_admin)
def lista_ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, "ciudades/lista_ciudades.html", {"ciudades": ciudades})