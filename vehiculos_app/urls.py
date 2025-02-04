"""vehiculos_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from home.views import signup, ReportesTemplateView
from propietarios import views

router = routers.DefaultRouter()
router.register(r'vehiculos', views.PropietariosViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('reportes/', ReportesTemplateView.as_view(), name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
    path('propietario/', include('propietarios.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^jet/', include('jet.urls', 'jet')),
]
