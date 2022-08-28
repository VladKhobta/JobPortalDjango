from rest_framework import routers, serializers, viewsets
from .models import Vacancy
from ..account.serializers import UserSerializer
# from ..account.models import User
from ..company.models import Company


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(queryset=Company.objects.all(), slug_field='user_id')
    company_designation = serializers.CharField(source='company.designation', read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'
