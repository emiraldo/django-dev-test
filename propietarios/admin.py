from django.contrib import admin

from propietarios.models import Propietario, VehiculoPropietario


class VehiculoInline(admin.StackedInline):
    model = VehiculoPropietario
    extra = 0
    raw_id_fields = 'modelo',


@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = 'numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento', 'usuario'
    list_display_links = 'numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento', 'usuario'
    search_fields = 'numero_documento',
    #readonly_fields = 'usuario',
    inlines = [
        VehiculoInline,
    ]
