from django.shortcuts import render
from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
# class UniversityViewSet(viewsets.ModelViewSet):
#     queryset = University.objects.all()
#     serializer_class = UniversitySerializer

class UserList(APIView):
    """List all student"""

    def get(self,request,format=None):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
