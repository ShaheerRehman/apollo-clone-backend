from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from .tasks import test_func
from rest_framework.viewsets import ModelViewSet
from .models import Person, Company
from .serializers import PersonSerializer, CompanySerializer
# Create your views here.
# def test(request):
#     test_func.delay()
#     return HttpResponse("Done")


class PersonGet(views.APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


class PersonCreate(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRetPutDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
