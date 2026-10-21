from django.contrib import admin
from .models import Localidad


@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ("pk_loc_id", "loc_nombre", "fk_eve", "loc_precio", "loc_cupo")
    search_fields = ("fk_eve__eve_nombre",)
    list_filter = ("loc_nombre", "fk_eve")
