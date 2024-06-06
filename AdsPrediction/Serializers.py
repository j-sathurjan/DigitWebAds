from rest_framework import serializers
from .models import TrainingData

class TrainingDataSerializer(serializers.Serializer):
    class Meta:
        model=TrainingData
        fields=['id','name','data_url']