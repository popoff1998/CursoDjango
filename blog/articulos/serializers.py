from rest_framework import serializers
from .models import Articulo, Comentario


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        exclude = []


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        exclude = []
