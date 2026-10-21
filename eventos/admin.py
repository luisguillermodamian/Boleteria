from django.contrib import admin
from localidades.models import Localidad
from .models import Evento


class LocalidadInline(admin.TabularInline):
    """Localidad es entidad débil de Evento: se registra dentro del evento."""
    model = Localidad
    extra = 3


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("pk_eve_id", "eve_nombre", "eve_fecha", "fk_lug", "eve_activo")
    search_fields = ("eve_nombre", "fk_lug__lug_nombre")
    list_filter = ("eve_activo", "fk_lug", "eve_fecha")
    inlines = [LocalidadInline]
