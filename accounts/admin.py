from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Ciudad


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Información extra", {"fields": ("rol", "ciudad")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Información extra", {"fields": ("rol", "ciudad")}),
    )
    list_display = ("username", "email", "rol", "ciudad", "is_staff", "is_superuser")


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")