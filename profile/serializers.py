from rest_framework import serializers
from .models import *
from .project_models import *

class DynamicFieldsModelSerializer(serializers.ModelSerializer):


    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class SkillDescriptionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = SkillDescription
        fields = ('id','skill_description')
        read_only_fields = ('id',)

class SkillTitlesSerializer(DynamicFieldsModelSerializer):


    class Meta:
        model = SkillTitle        
        fields = ('id', 'skill_title', 'skill_description')
        extra_kwargs = {'skill_description': {'required': False}}

class HobbySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hobby
        fields = ('id','name')
        read_only_fields = ('id',)


class TeamSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Team
        fields = ('id','name')
        read_only_fields = ('id',)


class DescriptionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'


class CompanySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProjectSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name','experience','company_key','description_key')     
        read_only_fields = ('id',)

class ProjectViewSerializer(DynamicFieldsModelSerializer):
    company_key = CompanySerializer(fields=['id','name'])
    description_key = DescriptionSerializer(fields=['id','info'],many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id','name','experience','company_key','description_key')     
        read_only_fields = ('id',)

class CandidateCreateSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Candidate
        fields = ('id','team_key', 'email','first_name', 'last_name', 'age', 'number', 'gender', 'projects', 'hobbies', 'experience', 'skill_title')
        read_only_fields = ('id',)

class CandidateListSerializer(DynamicFieldsModelSerializer):
    team_key = TeamSerializer(fields = ['id','name'])
    hobbies = HobbySerializer(fields=['id','name'], many=True, read_only=True)
    projects = ProjectSerializer(fields = ['id','name','experience','company_key','description_key'], many=True, read_only=True)
    skill_title = SkillTitlesSerializer(fields=['id','skill_title','skill_description'],many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = ('id','team_key', 'email','first_name', 'last_name', 'age', 'number', 'gender', 'projects', 'hobbies', 'experience', 'skill_title')
        read_only_fields = ('id',)



class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id','title','sub_title','illustrate')
        read_only_fields = ('id',)