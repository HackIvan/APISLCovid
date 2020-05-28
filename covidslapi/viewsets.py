from rest_framework import viewsets
from . import models
from . import serializers


class latestUpdateSLViewset(viewsets.ModelViewSet):
    queryset = models.latestUpdateSL.objects.all()
    serializer_class = serializers.latestUpdateSLSerializer


class districtCasesViewset(viewsets.ModelViewSet):
    queryset = models.districtCases.objects.all()
    serializer_class = serializers.districtCasesSerializer