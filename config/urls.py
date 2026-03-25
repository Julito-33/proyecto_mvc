from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from accounts.forms import LoginForm
from accounts.views import (
    home,
    crear_usuario,
    lista_usuarios,
    crear_ciudad,
    lista_ciudades,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", RedirectView.as_view(pattern_name="login", permanent=False)),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=LoginForm
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("panel/", home, name="home"),

    path("usuarios/", lista_usuarios, name="lista_usuarios"),
    path("usuarios/nuevo/", crear_usuario, name="crear_usuario"),

    path("ciudades/", lista_ciudades, name="lista_ciudades"),
    path("ciudades/nueva/", crear_ciudad, name="crear_ciudad"),
]