from django.urls import path

from propietarios.views import VehiculosPropietarioListView, PropietariosCreateView, PropietarioUpdateView, \
    VehiculoPropietarioCreateView, VehiculoPropietarioUpdateView, VehiculoPropietarioDeleteView

urlpatterns = [
    path('mis-vehiculos/', VehiculosPropietarioListView.as_view(), name='vehiculos-list'),
    path('crear-perfil/', PropietariosCreateView.as_view(), name='crear-propietario'),
    path('actualizar-perfil/<pk>/', PropietarioUpdateView.as_view(), name='editar-propietario'),
    path('nuevo-vehiculo/', VehiculoPropietarioCreateView.as_view(), name='crear-vehiculo'),
    path('editar-vehiculo/<pk>/', VehiculoPropietarioUpdateView.as_view(), name='editar-vehiculo'),
    path('eliminar-vehiculo/<pk>/', VehiculoPropietarioDeleteView.as_view(), name='eliminar-vehiculo'),
]
