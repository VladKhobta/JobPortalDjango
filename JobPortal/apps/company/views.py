from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import CompanySerializer
from .models import Company


class CompanyView(APIView):

    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        serializer = CompanySerializer(company)
        return Response({'company': serializer.data})

    def put(self, request, pk):
        company = Company.objects.get(pk=pk)
        data = request.data.get('company')
        serializer = CompanySerializer(instance=company, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = get_object_or_404(Company.objects.all(), pk=pk)
        company.delete()
        return Response({"message": "Company with id `{}` has been deleted.".format(pk)}, status=204)
