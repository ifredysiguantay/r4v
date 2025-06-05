from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    status = serializers.CharField()
    total = serializers.IntegerField()