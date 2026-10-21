from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("pk_cli_id", "cli_nombre", "cli_documento", "cli_correo", "cli_telefono")
    search_fields = ("cli_nombre", "cli_documento", "cli_correo")
    list_filter = ("cli_nombre",)
