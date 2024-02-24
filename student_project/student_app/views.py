from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404


class StudentAPI(APIView):
    def get(self, request):
        try:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'error show on data fetching'}, status=400)
    
    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=201)
        except:
            return Response(data=serializer.errors, status=400)
        
class StudentDetailsAPI(APIView):
    def get(self, request, pk=None):
        try:
            students = Student.objects.get(pk=pk)
            serializer = StudentSerializer(data=request.data, instance=students)
            return Response(data=serializer.data, status=201)
        except:
            return Response(data={'details':'fetching time error'}, status=400)
        
    def put(self, request, pk=None):
        try:
            students = Student.objects.get(pk=pk)
            serializer = StudentSerializer(data=request.data, instance=students)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=205)
        except:
            return Response(data=serializer.errors, status=400)
    