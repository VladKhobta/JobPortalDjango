from rest_framework import routers, serializers, viewsets
from .models import Company
from ..account.serializers import UserSerializer
from ..account.models import User


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True, many=False)

    class Meta:
        model = Company
        fields = ['designation', 'description', 'establishment_date', 'website_url', 'user']

    def update(self, instance, validated_data):
        vd = validated_data

        instance.designation = vd.get('designation', instance.designation)
        instance.description = vd.get('description', instance.description)
        instance.establishment_date = vd.get('establishment_date', instance.establishment_date)
        instance.website_url = vd.get('website_url', instance.website_url)
        print(instance.user)

        instance.save()
        return instance
