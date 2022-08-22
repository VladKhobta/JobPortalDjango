from rest_framework import routers, serializers, viewsets
from .models import Vacancy
from ..account.serializers import UserSerializer
# from ..account.models import User
from ..company.models import Company


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(queryset=Company.objects.all(), slug_field='user_id')
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'
    #
    # def create(self, validated_data):
    #     # pk = validated_data.get('company_id')
    #     print(validated_data.get('title'))
    #     print(2222)
    #     print(validated_data.get('company_id'))
    #     company = Company.objects.get(pk=validated_data.get('company_id'))
    #     vacancy = Vacancy.objects.create(company=company)
    #     vacancy.save()
    #     return vacancy

