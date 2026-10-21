from django.db import models


class Compra(models.Model):
    pk_com_id = models.AutoField(primary_key=True)
    com_fecha = models.DateTimeField()
    com_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    com_metodo_pago = models.CharField(
        max_length=20,
        choices=[("EFECTIVO", "Efectivo"), ("TARJETA", "Tarjeta"), ("TRANSFERENCIA", "Transferencia")],
    )
    fk_cli = models.ForeignKey(
        "clientes.Cliente", on_delete=models.PROTECT, db_column="fk_cli_id", related_name="compras"
    )
    # Relación N:M Compra - Localidad, resuelta con la tabla intermedia DetalleCompra
    localidades = models.ManyToManyField(
        "localidades.Localidad", through="detalles_compra.DetalleCompra", related_name="compras"
    )

    class Meta:
        db_table = "tbl_compra"

    def __str__(self):
        return f"Compra #{self.pk_com_id} - {self.fk_cli.cli_nombre}"
