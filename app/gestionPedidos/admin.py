from django.contrib import admin

from gestionPedidos.models import Clientes,Articulos,Pedidos
# Register your models here.

# Clase utilizada para agregar campos al admin Django
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","fono")
    search_fields=("nombre","fono")

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)