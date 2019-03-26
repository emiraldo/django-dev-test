from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from vehiculos.models import Marca, Modelo, Tipo


@admin.register(Marca)
class MarcaAdmin(ImportExportModelAdmin):
    list_display = 'nombre',
    list_display_links = 'nombre',


@admin.register(Modelo)
class ModeloAdmin(ImportExportModelAdmin):
    list_display = 'nombre', 'marca'
    list_display_links = 'nombre', 'marca'
    list_filter = 'marca',


@admin.register(Tipo)
class TipoAdmin(ImportExportModelAdmin):
    list_display = 'nombre',
    list_display_links = 'nombre',
