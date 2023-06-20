from rest_framework import serializers

from apps.meseros.models import Meseros


class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meseros
        fields = ('nacionalidad','nombre','edad','procedencia')
