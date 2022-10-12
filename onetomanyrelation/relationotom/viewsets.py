from rest_framework import viewsets
from . import models
from . import serializers

class phoneViewset(viewsets.ModelViewSet):
    queryset = models.phone.objects.all()
    serializer_class = serializers.phoneSerializer

class personViewset(viewsets.ModelViewSet):
    queryset = models.person.objects.all()
    serializer_class = serializers.personSerializer

class aadarViewset(viewsets.ModelViewSet):
    queryset = models.aadar.objects.all()
    serializer_class = serializers.aadarSerializer