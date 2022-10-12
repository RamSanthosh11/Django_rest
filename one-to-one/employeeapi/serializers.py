from rest_framework import serializers
from .models import Employee,vehicle

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = '__all__'

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model =vehicle
        fields = '__all__'