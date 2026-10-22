# Sistema de Boletería de Eventos

Sistema en Django para vender entradas a eventos: registra lugares, eventos, localidades
de cada evento (VIP, general, preferencial) con su precio y cupo, clientes y compras de entradas.

## Actores
Administrador, Organizador, Taquillero y Cliente 

## Modelo de datos
| App | Tabla | Descripción |
|---|---|---|
| `lugares` | `tbl_lugar` | Sitios donde se realizan los eventos |
| `eventos` | `tbl_evento` | Eventos (1:N con Lugar) |
| `localidades` | `tbl_localidad` | Entidad débil de Evento: "VIP del evento X", con precio y cupo |
| `clientes` | `tbl_cliente` | Compradores |
| `compras` | `tbl_compra` | Compras (1:N con Cliente) |
| `detalles_compra` | `tbl_detalle_compra` | Tabla intermedia de la relación N:M Compra–Localidad (cantidad, precio unitario) |

En el admin, las localidades se agregan como inline dentro del evento y los renglones (detalles) dentro de la compra.

## Cómo ejecutarlo
```
 python manage.py runserver
```


Abrir http://127.0.0.1:8000/admin/



## Credenciales del administrador
- Usuario: `admin`
- Contraseña: `Admin2026*`

## Estructura
```
boleteria/
├── config/            # settings.py, urls.py
├── lugares/  eventos/  localidades/  clientes/  compras/  detalles_compra/
├── docs/              # diagrama_actores.png, diagrama_er.png
├── manage.py
├── requirements.txt
└── README.md
```

## Integrantes
-jorge cordoba
-luis damian 
-daniel cordero
