from django.shortcuts import render
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


class AdvocateList(APIView, MyPaginationMixin):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    # We need to override the get method to insert pagination
    def get(self, request):
        ...
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)


class AdvocateDetail(APIView):
    def get(self, request, pk):
        advocate = Advocate.objects.get(username=pk)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
