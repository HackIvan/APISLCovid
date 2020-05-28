from rest_framework import serializers
from .models import latestUpdateSL
from .models import districtCases

class latestUpdateSLSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = latestUpdateSL
        fields = '__all__'



class districtCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = districtCases
        fields = '__all__'


 