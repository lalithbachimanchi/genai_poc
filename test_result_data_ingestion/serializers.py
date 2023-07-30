from rest_framework import serializers
from .models import *


class PerformanceTestResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceTestResults
        fields = '__all__'