from django.contrib import admin
from detalles_compra.models import DetalleCompra
from .models import Compra


class DetalleCompraInline(admin.TabularInline):
    """Los renglones de la compra se registran dentro de la compra."""
    model = DetalleCompra
    extra = 2


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("pk_com_id", "fk_cli", "com_fecha", "com_total", "com_metodo_pago")
    search_fields = ("fk_cli__cli_nombre", "fk_cli__cli_documento")
    list_filter = ("com_metodo_pago", "com_fecha")
    inlines = [DetalleCompraInline]
