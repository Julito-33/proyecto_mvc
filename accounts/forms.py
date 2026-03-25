from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "Ingresa tu usuario",
                "autocomplete": "username",
            }
        ),
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Ingresa tu contraseña",
                "autocomplete": "current-password",
            }
        ),
    )