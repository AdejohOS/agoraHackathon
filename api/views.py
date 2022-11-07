from rest_framework import generics
from rest_framework.response import Response

from rest_framework.settings import api_settings
from rest_framework.views import APIView
from.mixin import MyPaginationMixin

from . serializers import AdvocateSerializer

from advocate.models import Advocate

from rest_framework import filters


class ApiEndpoints(APIView):
    def get(self, request):

        routes = [
            'https://api-hackathon.up.railway.app/advocates',
            'https://api-hackathon.up.railway.app/advocates/brown071'
        ]
        return Response(routes)


class AdvocateList(generics.ListAPIView):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AdvocateSerializer
    queryset = Advocate.objects.all()


class AdvocateDetail(APIView):
    def get(self, request, pk):
        advocate = Advocate.objects.get(username=pk)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
