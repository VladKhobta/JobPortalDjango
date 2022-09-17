from rest_framework import serializers
from .models import ResponseVacancy


class ResponseSerializer(serializers.ModelSerializer):
    candidate_first_name = serializers.CharField(source='candidate.first_name', read_only=True)
    candidate_last_name = serializers.CharField(source='candidate.last_name', read_only=True)
    vacancy_title = serializers.CharField(source='vacancy.title', read_only=True)

    class Meta:
        model = ResponseVacancy
        fields = '__all__'

    # def create(self, validated_data):
    #     vd = validated_data
    #     response =

