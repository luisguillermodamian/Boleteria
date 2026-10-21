from django.db import models


class Localidad(models.Model):
    """Entidad débil: 'VIP del evento X'. Su identidad depende del evento."""
    pk_loc_id = models.AutoField(primary_key=True)
    loc_nombre = models.CharField(
        max_length=20,
        choices=[("VIP", "VIP"), ("GENERAL", "General"), ("PREFERENCIAL", "Preferencial")],
    )
    loc_precio = models.DecimalField(max_digits=10, decimal_places=2)
    loc_cupo = models.IntegerField()
    fk_eve = models.ForeignKey(
        "eventos.Evento", on_delete=models.CASCADE, db_column="fk_eve_id", related_name="localidades"
    )

    class Meta:
        db_table = "tbl_localidad"
        verbose_name_plural = "localidades"
        constraints = [
            models.UniqueConstraint(fields=["fk_eve", "loc_nombre"], name="uq_localidad_evento")
        ]

    def __str__(self):
        return f"{self.get_loc_nombre_display()} de {self.fk_eve.eve_nombre}"
