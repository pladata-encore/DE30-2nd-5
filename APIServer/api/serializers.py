from rest_framework import serializers
from .models import UserSymptoms, RequestDisease


class UserSymptomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSymptoms
        fields = '__all__'


class RequestDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDisease
        fields = '__all__'
