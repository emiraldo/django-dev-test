from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
import numpy as np
import pandas as pd


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


class ReportesTemplateView(TemplateView):
    template_name = 'reportes/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehiculos = pd.read_csv('http://devtest-liftit.herokuapp.com/api/vehiculos.csv')
        vehiculos_marca = vehiculos.groupby('modelo_marca').count()[['id']]
        vehiculos_marca.columns = ['']
        context['vehiculos_marca'] = vehiculos_marca.to_html(header=True, index_names=False, table_id='tabla-cantidades')
        context['vehiculos'] = pd.read_json('https://devtest-liftit.herokuapp.com/api/vehiculos.json')
        return context
