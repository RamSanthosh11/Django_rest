from rest_framework import serializers
from .models import aadar, person,phone

class personSerializer(serializers.ModelSerializer):
    class Meta:
        model =person
        fields = '__all__'

class phoneSerializer(serializers.ModelSerializer):
    class Meta:
        model =phone
        fields = '__all__'

class aadarSerializer(serializers.ModelSerializer):
    class Meta:
        model =aadar
        fields = '__all__'