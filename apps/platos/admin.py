from django.contrib import admin
from apps.platos.models import Platos
# Register your models here.
@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)

