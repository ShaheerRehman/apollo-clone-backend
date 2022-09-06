from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from rest_framework.viewsets import ModelViewSet
from .models import Person, Company
from .serializers import PersonSerializer, CompanySerializer
# Create your views here.
# def test(request):
#     test_func.delay()
#     return HttpResponse("Done")


class PersonView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer