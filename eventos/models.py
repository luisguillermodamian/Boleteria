from django.db import models


class Evento(models.Model):
    pk_eve_id = models.AutoField(primary_key=True)
    eve_nombre = models.CharField(max_length=120)
    eve_descripcion = models.TextField(blank=True)
    eve_fecha = models.DateTimeField()
    eve_activo = models.BooleanField(default=True)
    fk_lug = models.ForeignKey(
        "lugares.Lugar", on_delete=models.PROTECT, db_column="fk_lug_id", related_name="eventos"
    )

    class Meta:
        db_table = "tbl_evento"

    def __str__(self):
        return f"{self.eve_nombre} - {self.eve_fecha:%d/%m/%Y}"
