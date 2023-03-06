from django.db import models
from accounts.models import DateTimeMixin

## Project Description
class Description(DateTimeMixin):
    info = models.TextField(blank=True)

    def __str__(self):
        return str(self.info)

## which place candidate work
class Company(DateTimeMixin):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.name)


## Project Information of candidate in terms of project
class Project(DateTimeMixin):
    company_key = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    description_key = models.ManyToManyField(Description, blank=True)
    experience = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.name)



