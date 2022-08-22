from rest_framework import routers, serializers, viewsets
from .models import User
from ..candidate.models import Candidate
from ..company.models import Company


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'user_type', 'is_staff', 'date_joined', 'password']

    def create(self, validated_data):
        vd = validated_data
        user = User.objects.create(
            email=vd['email'],
            user_type=vd['user_type'],
            phone_number=vd['phone_number']
        )
        user.set_password(vd['password'])
        user.save()

        if vd['user_type'] == 'APPLICANT':
            candidate = Candidate.objects.create(user=user)
            candidate.save()
        if vd['user_type'] == 'COMPANY':
            company = Company.objects.create(user=user, designation=vd['designation'])
            company.save()

        return user

    def update(self, instance, validated_data):
        vd = validated_data
        instance.email = vd.get('email', instance.email)
        instance.phone_number = vd.get('phone_number', instance.phone_number)

        instance.save()
        return instance
