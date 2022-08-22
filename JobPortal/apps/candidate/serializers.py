from rest_framework import routers, serializers, viewsets
from .models import Candidate
from ..account.serializers import UserSerializer
from ..account.models import User


class CandidateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True, many=False)

    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'current_salary', 'user']

    def update(self, instance, validated_data):
        vd = validated_data

        instance.first_name = vd.get('first_name', instance.first_name)
        instance.last_name = vd.get('last_name', instance.last_name)
        instance.current_salary = vd.get('current_salary', instance.current_salary)
        print(instance.user)

        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     partial = True
    #     print(19)
    #     vd = validated_data
    #     user_data = vd.pop['user']
    #     pk = self.user_data['id']
    #     print(7)
    #     user = User.objects.get(pk=pk)
    #     print(user)
    #     user_serializer = UserSerializer.update(user, data=user_data)
    #     if user_serializer.is_valid():
    #         user_serializer.update(user, user_data)
    #     instance.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     print(5)
    #     # saved_user = User.objects.get(pk=validated_data['user']['id'])
    #     return 'success'# saved_user