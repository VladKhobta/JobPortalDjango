from rest_framework import serializers
from .models import AnswerToVacancy, AnswerToCandidate


class AnswerToVacancySerializer(serializers.ModelSerializer):
    candidate_first_name = serializers.CharField(source='candidate.first_name', read_only=True)
    candidate_last_name = serializers.CharField(source='candidate.last_name', read_only=True)
    vacancy_title = serializers.CharField(source='vacancy.title', read_only=True)

    class Meta:
        model = AnswerToVacancy
        fields = '__all__'

    def validate(self, data):
        if AnswerToVacancy.objects.get(candidate=data['candidate'], vacancy=data['vacancy']):
            raise serializers.ValidationError('This candidate already had replied to this vacancy')
        return data
    # def validate_candidate(self, value):
    #     if ResponseVacancy.objects.get(candidate=value, company=)

    # def create(self, validated_data):
    #      vd = validated_data
    #      if ResponseVacancy.objects.get


class AnswerToCandidateSerializer(serializers.ModelSerializer):
    candidate_pk = serializers.CharField(source="answer_to_vacancy.candidate.pk", read_only=True)

    class Meta:
        model = AnswerToCandidate
        fields = '__all__'

    def create(self, validated_data):
        vd = validated_data
        print(vd['answer_to_vacancy'])
        candidate_pk = AnswerToVacancy.objects.get(pk=vd['answer_to_vacancy'].pk).candidate
        answer = AnswerToCandidate.objects.create(
            answer_to_vacancy=vd['answer_to_vacancy'],
            candidate=candidate_pk,
            message=vd['message'],
            decision=vd['decision'],
        )
        answer.save()

        return answer
