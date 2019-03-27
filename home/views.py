import pandas as pd
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class ReportesTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehiculos = pd.read_csv('https://devtest-liftit.herokuapp.com/api/vehiculos.csv')
        vehiculos_marca = vehiculos.groupby('modelo_marca').count()[['id']]
        vehiculos_marca.columns = ['']
        vehiculos_tabla = vehiculos[['id', 'modelo_marca', 'modelo_nombre', 'tipo_nombre', 'placa']]
        vehiculos_tabla.columns = ['Id', 'Marca', 'Modelo', 'Tipo', 'Placa']
        context['vehiculos_marca'] = vehiculos_marca.to_html(header=True, index_names=False,
                                                             table_id='tabla-cantidades')
        context['vehiculos'] = vehiculos_tabla.to_html(table_id='example', index=False)
        context['active'] = 'reportes'
        return context
