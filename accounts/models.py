from django.contrib.auth.models import AbstractUser
from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    ROLES = (
        ("admin", "Administrador"),
        ("normal", "Usuario normal"),
    )

    rol = models.CharField(max_length=10, choices=ROLES, default="normal")
    ciudad = models.ForeignKey(
        Ciudad,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="usuarios"
    )

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.rol = "admin"
            self.is_staff = True
        else:
            self.is_staff = self.rol == "admin"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username