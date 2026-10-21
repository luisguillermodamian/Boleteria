from django.db import models


class DetalleCompra(models.Model):
    pk_det_id = models.AutoField(primary_key=True)
    det_cantidad = models.IntegerField()
    det_precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    fk_com = models.ForeignKey(
        "compras.Compra", on_delete=models.CASCADE, db_column="fk_com_id", related_name="detalles"
    )
    fk_loc = models.ForeignKey(
        "localidades.Localidad", on_delete=models.PROTECT, db_column="fk_loc_id", related_name="detalles"
    )

    class Meta:
        db_table = "tbl_detalle_compra"
        verbose_name_plural = "detalles de compra"

    def save(self, *args, **kwargs):
        if self.det_precio_unitario is None:
            self.det_precio_unitario = self.fk_loc.loc_precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.det_cantidad} x {self.fk_loc}"
