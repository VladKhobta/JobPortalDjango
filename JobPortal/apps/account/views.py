from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .models import User


class UserView(APIView):
    # def get(self, request):
    #     print('list get')
    #     users = User.objects.all().order_by("date_joined")
    #     serializer = UserSerializer(users, many=True)
    #     return Response({'users': serializer.data})

    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)

    def get(self, request, pk=None):
        if pk is None:
            users = User.objects.all().order_by("date_joined")
            serializer = UserSerializer(users, many=True)
            return Response({'users': serializer.data})
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({'success': "User '{}' created successfully.".format(user_saved.email)})

    def put(self, request, pk):
        saved_user = User.objects.get(pk=pk)
        data = request.data.get('user')
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            saved_user = serializer.save()

        return Response({"success": "User '{}' updated successfully.".format(saved_user.email)})

    def delete(self, request, pk):
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, status=204)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'phone_number': user.phone_number,
            'user_type': user.user_type,
        })
