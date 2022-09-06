from .models import Person, Company
from rest_framework.serializers import ModelSerializer


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

