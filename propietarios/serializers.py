from rest_framework import serializers

from propietarios.models import VehiculoPropietario


class PropietarioSerializer(serializers.ModelSerializer):
    modelo_nombre = serializers.ReadOnlyField(source='modelo.nombre')
    modelo_marca = serializers.ReadOnlyField(source='modelo.marca.nombre')
    propietario_nombres = serializers.ReadOnlyField(source='propietario.nombres')
    propietario_apellidos = serializers.ReadOnlyField(source='propietario.apellidos')
    tipo_nombre = serializers.ReadOnlyField(source='tipo.nombre')

    class Meta:
        model = VehiculoPropietario
        fields = 'id', 'propietario_nombres', 'propietario_apellidos', 'modelo_marca', 'modelo_nombre', 'tipo_nombre', 'placa'


class VehiculoPropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoPropietario
        fields = 'placa'
