from django.db import models


class Lugar(models.Model):
    pk_lug_id = models.AutoField(primary_key=True)
    lug_nombre = models.CharField(max_length=100)
    lug_ciudad = models.CharField(max_length=80)
    lug_direccion = models.CharField(max_length=150)
    lug_capacidad = models.IntegerField()

    class Meta:
        db_table = "tbl_lugar"
        verbose_name_plural = "lugares"

    def __str__(self):
        return f"{self.lug_nombre} ({self.lug_ciudad})"
