from rest_framework import serializers
from .models import Place, University

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = University
        fields = '__all__'