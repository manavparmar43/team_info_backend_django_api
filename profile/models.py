from django.db import models
from accounts.models import DateTimeMixin

from .project_models import *

# Create your models here.



## Hobby particular so that we dont have to recreate
class Hobby(DateTimeMixin):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

## Team Information like python, php
class Team(DateTimeMixin):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class SkillDescription(models.Model):
    skill_description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.skill_description

class SkillTitle(DateTimeMixin):
    skill_title = models.CharField(max_length=250, null=True, blank=True)
    skill_description = models.ManyToManyField(SkillDescription, blank=True)

    def __str__(self):
        return self.skill_title


Gender = (
    ("M","MALE"),
    ("F","FEMALE"),
)

#particular candidate profile 
class Candidate(DateTimeMixin):
    team_key   = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=250, blank=True)
    last_name  = models.CharField(max_length=250, blank=True)
    age        = models.IntegerField(blank=True, null=True)
    email      = models.EmailField(blank=True)
    number     = models.IntegerField(blank=True)
    gender     = models.CharField(choices=Gender, blank=True, max_length=10)
    projects   = models.ManyToManyField(Project, blank=True)
    hobbies    = models.ManyToManyField(Hobby, blank=True)
    experience = models.IntegerField(blank=True)
    skill_title = models.ManyToManyField(SkillTitle, blank=True)
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Content(DateTimeMixin):
    title = models.CharField(max_length=250, null=True, blank=True)
    sub_title = models.CharField(max_length=250, null=True, blank=True)
    illustrate = models.TextField(null=True, blank=True, verbose_name="Content")

    def __str__(self):
        return self.title

