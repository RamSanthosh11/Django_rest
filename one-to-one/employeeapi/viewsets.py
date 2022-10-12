from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

class vehicleViewset(viewsets.ModelViewSet):
    queryset = models.vehicle.objects.all()
    serializer_class = serializers.vehicleSerializer