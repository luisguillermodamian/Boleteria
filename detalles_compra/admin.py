from django.contrib import admin
from .models import DetalleCompra


@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ("pk_det_id", "fk_com", "fk_loc", "det_cantidad", "det_precio_unitario")
    search_fields = ("fk_com__fk_cli__cli_nombre", "fk_loc__fk_eve__eve_nombre")
    list_filter = ("fk_loc__loc_nombre",)
