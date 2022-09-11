from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CandidateSerializer
from .models import Candidate
from .permissions import IsOwner


class CandidateView(APIView):

    permission_classes = [IsOwner]

    def get(self, request, pk):
        candidate = Candidate.objects.get(pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response({'candidate': serializer.data})

    def put(self, request, pk):
        candidate = Candidate.objects.get(pk=pk)
        data = request.data.get('candidate')
        serializer = CandidateSerializer(instance=candidate, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
