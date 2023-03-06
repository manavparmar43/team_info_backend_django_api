from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User



# Create your views here.
class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

class SkillDescriptionViewSet(viewsets.ModelViewSet):
    queryset = SkillDescription.objects.all()
    serializer_class = SkillDescriptionSerializer

class SkillTitleViewSet(viewsets.ModelViewSet):
    queryset=SkillTitle.objects.all()
    serializer_class = SkillTitlesSerializer
    
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=['get'])
    def get_candidate(self, request, pk = None):
        candidate = Candidate.objects.filter(team_key = pk)
        serializer = CandidateListSerializer(instance = candidate, many = True)
        return Response(serializer.data)




class CandidateCreateViewAPI(ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateCreateSerializer


class CandidateListViewAPI(ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateListSerializer

class ProjectDescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ProjectCreateViewAPI(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectViewAPI(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectViewSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class UserCreate(generics.CreateAPIView):
    def post(self, request):
        user = User.objects.create_superuser(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response("user created successfully")


# def create_user(request):

#     username = request.data['username']
#     password = request.data['password']

#     print(username)
#     print(password)

#     # user = User.objects.create(username = username, password = password)




#     return Response("created")