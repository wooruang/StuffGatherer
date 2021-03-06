from rest_framework import serializers
from .models import Data, Status


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'sub_category',
            'origin',
            'content',
        )
        model = Data


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'data',
            'status'
        )
        model = Status
