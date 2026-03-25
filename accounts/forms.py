from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario, Ciudad


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            "class": "input",
            "placeholder": "Ingresa tu usuario"
        })
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "input",
            "placeholder": "Ingresa tu contraseña"
        })
    )


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "ciudad",
            "rol",
            "password1",
            "password2",
        ]


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ["nombre"]