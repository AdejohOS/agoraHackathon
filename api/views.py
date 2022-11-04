from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework import generics
from . serializers import AdvocateSerializer

from advocate.models import Advocate

from rest_framework import filters


@api_view(['GET'])
def ApiEndpoints(request):

    routes = [
        'https://api-hackathon.up.railway.app/advocates',
        'https://api-hackathon.up.railway.app/advocates/id'
    ]
    return Response(routes)


class AdvocateList(generics.ListAPIView):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AdvocateSerializer
    queryset = Advocate.objects.all()
       


class AdvocateDetail(generics.RetrieveAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
