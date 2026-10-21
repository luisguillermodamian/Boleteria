from django.contrib import admin
from .models import Lugar


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ("pk_lug_id", "lug_nombre", "lug_ciudad", "lug_direccion", "lug_capacidad")
    search_fields = ("lug_nombre", "lug_ciudad")
    list_filter = ("lug_ciudad",)
