from rest_framework import serializers
from .models import Response


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = '__all__'

    # def create(self, validated_data):
    #     vd = validated_data
    #     response =

