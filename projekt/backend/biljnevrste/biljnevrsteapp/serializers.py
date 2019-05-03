from rest_framework import serializers
from .models import *


class UporabniDioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UporabniDio
        fields = '__all__'


class SlikaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slika
        fields = '__all__'


class RodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rod
        fields = '__all__'


class SistematicarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sistematicar
        fields = '__all__'


class BiljnaVrstaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BiljnaVrsta
        fields = '__all__'


class PorodicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Porodica
        fields = '__all__'


class PodvrstaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podvrsta
        fields = '__all__'


class VarijetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Varijet
