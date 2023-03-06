from django.urls import path,include
from .views import *
urlpatterns = [
    path('project/',ProjectCreateViewAPI.as_view(), name='project'),      
    path('project-list/',ProjectViewAPI.as_view(),name='project-list'), 
    path('candidate-create/',CandidateCreateViewAPI.as_view(),name='candidate-create'), 
    path('candidate-list/',CandidateListViewAPI.as_view(),name='candidate-list'), 
]