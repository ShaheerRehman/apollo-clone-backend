from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    hqLocation = models.CharField(max_length=128)
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    job = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=128)
    location = models.CharField(max_length=128)
    employees = models.IntegerField(default=0)
    industry = models.CharField(max_length=128)
    ## Assuming that on person can belong to only on company but one company can have many people.
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def companyName(self):
        comp = Company.objects.get(name=self.company).name
        hq = Company.objects.get(name=self.company).hqLocation
        type = Company.objects.get(name=self.company).type
        return {'name': comp, 'headquarters': hq, 'type': type }


    def __str__(self):
        return self.name
