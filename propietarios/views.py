from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from rest_framework import viewsets

from propietarios.models import VehiculoPropietario, Propietario
from propietarios.serializers import PropietarioSerializer


class PropietariosViewSet(viewsets.ModelViewSet):
    serializer_class = PropietarioSerializer
    queryset = VehiculoPropietario.objects.all()
    pagination_class = None


class PropietarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Propietario
    fields = 'numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento', 'soporte_documento'
    success_url = reverse_lazy('vehiculos-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PropietarioUpdateView, self).get_context_data(**kwargs)
        context['active'] = 'perfil'
        return context


class PropietariosCreateView(LoginRequiredMixin, CreateView):
    model = Propietario
    fields = 'numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento', 'soporte_documento'
    success_url = reverse_lazy('vehiculos-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        existe = Propietario.objects.filter(usuario=self.request.user).first()
        if existe:
            form.add_error(None, ValidationError({"numero_documento": "El usuario ya tiene un propietario registrado"}))
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PropietariosCreateView, self).get_context_data(**kwargs)
        context['active'] = 'perfil'
        return context


class VehiculosPropietarioListView(LoginRequiredMixin, ListView):
    model = VehiculoPropietario
    paginate_by = 10

    def get_queryset(self):
        return VehiculoPropietario.objects.filter(propietario__usuario=self.request.user).order_by('modelo__marca')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VehiculosPropietarioListView, self).get_context_data(**kwargs)
        context['active'] = 'vehiculos-list'
        return context


class VehiculoPropietarioCreateView(LoginRequiredMixin, CreateView):
    model = VehiculoPropietario
    fields = 'modelo', 'tipo', 'placa'
    success_url = reverse_lazy('vehiculos-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VehiculoPropietarioCreateView, self).get_context_data(**kwargs)
        context['active'] = 'vehiculos-list'
        return context

    def form_valid(self, form):
        existe = Propietario.objects.filter(usuario=self.request.user).first()
        if existe:
            form.instance.propietario = existe
            return super().form_valid(form)
        form.add_error(None, ValidationError({"modelo": "Antes de crear un vehiculo, debe crear su perfil."}))
        return super().form_invalid(form)


class VehiculoPropietarioUpdateView(LoginRequiredMixin, UpdateView):
    model = VehiculoPropietario
    fields = 'modelo', 'tipo', 'placa'
    success_url = reverse_lazy('vehiculos-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VehiculoPropietarioUpdateView, self).get_context_data(**kwargs)
        context['active'] = 'vehiculos-list'
        return context


class VehiculoPropietarioDeleteView(DeleteView):
    model = VehiculoPropietario
    success_url = reverse_lazy('vehiculos-list')
