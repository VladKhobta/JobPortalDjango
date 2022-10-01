from rest_framework import serializers
from .models import ResponseToVacancy, ResponseToCandidate


class ResponseToVacancySerializer(serializers.ModelSerializer):
    candidate_first_name = serializers.CharField(source='candidate.first_name', read_only=True)
    candidate_last_name = serializers.CharField(source='candidate.last_name', read_only=True)
    vacancy_title = serializers.CharField(source='vacancy.title', read_only=True)

    class Meta:
        model = ResponseToVacancy
        fields = '__all__'

    def validate(self, data):
        if ResponseToVacancy.objects.get(candidate=data['candidate'], vacancy=data['vacancy']):
            raise serializers.ValidationError('This candidate already had replied to this vacancy')
        return data
    # def validate_candidate(self, value):
    #     if ResponseVacancy.objects.get(candidate=value, company=)

    # def create(self, validated_data):
    #      vd = validated_data
    #      if ResponseVacancy.objects.get


class ResponseToCandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseToCandidate
        fields = '__all__'

