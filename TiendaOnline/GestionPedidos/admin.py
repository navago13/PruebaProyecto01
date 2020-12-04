from django.contrib import admin
from GestionPedidos.models import CLIENTES,ARTICULOS,PEDIDOS

# Register your models here.
# cuando se realizan cambios en admin.py hay que reiniciar el servidor
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","telefono")
# para tener una casilla de busqueda por nombre y telefono
    search_fields=("nombre","telefono")

class ArticulosAdmin(admin.ModelAdmin):
    # como al final porque es una tupa
    list_filter=("seccion",)
    list_display=("nombrearticulo","seccion","precioarticulo")

   # search_fields=("nombrearticulo","seccion")

class PedidosAdmin(admin.ModelAdmin):
    # como al final porque es una tupa
    list_filter=("fechadepedido",)
    date_hierarchy="fechadepedido"
    list_display=("numerodepedido","fechadepedido","entrgapedido")


admin.site.register(CLIENTES,ClientesAdmin)
# hay que indicar que se va a utilar esta clase
admin.site.register(ARTICULOS,ArticulosAdmin)

admin.site.register(PEDIDOS,PedidosAdmin)

