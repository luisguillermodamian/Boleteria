from django.db import models


class Cliente(models.Model):
    pk_cli_id = models.AutoField(primary_key=True)
    cli_nombre = models.CharField(max_length=100)
    cli_documento = models.CharField(max_length=20, unique=True)
    cli_correo = models.EmailField(max_length=120)
    cli_telefono = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = "tbl_cliente"

    def __str__(self):
        return f"{self.cli_nombre} ({self.cli_documento})"
