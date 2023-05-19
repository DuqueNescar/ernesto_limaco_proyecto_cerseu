from django.contrib import admin
from clientes.models import Clientes
# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni')
    list_filter = ('nombre',)
    search_fields = ('nombre','dni',)

