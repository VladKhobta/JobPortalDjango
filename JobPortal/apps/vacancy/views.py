from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import VacancySerializer
from .models import Vacancy


class VacancyView(APIView):

    def post(self, request):
        vacancy_data = request.data

        serializer = VacancySerializer(data=vacancy_data)
        print(1)
        if serializer.is_valid(raise_exception=True):
            vacancy_saved = serializer.save()

        return Response({"success": "Vacancy '{}' created successfully".format(vacancy_saved.title)})

    def get(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)
        serializer = VacancySerializer(vacancy)
        return Response({'vacancy': serializer.data})

    def put(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)
        data = request.data
        serializer = VacancySerializer(instance=vacancy, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyListView(APIView):

    def get(self, request, pk):
        if pk is None:
            vacancies = Vacancy.objects.all()
            print(vacancies)
            serializer = VacancySerializer(vacancies, many=True)
            return Response({'vacancies': serializer.data})
        vacancies = Vacancy.objects.filter(company=pk)
        serializer = VacancySerializer(vacancies, many=True)
        return Response({'vacancies': serializer.data})

    def put(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)
        data = request.data
        serializer = VacancySerializer(instance=vacancy, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancySearchView(APIView):

    def get(self, request, filter):
        vacancies = Vacancy.objects.filter(title__contains=filter)
        serializer = VacancySerializer(vacancies, many=True)
        return Response({'vacancies': serializer.data})
