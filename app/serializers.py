from .models import Person, Company
from rest_framework.serializers import ModelSerializer


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['name','job', 'email','location' ,'employees','industry', 'company', 'companyName']
        read_only_fields = ['companyName',]


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

