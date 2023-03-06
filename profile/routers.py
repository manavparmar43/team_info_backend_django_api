from rest_framework.routers import DefaultRouter
from .views import *

from django.urls import path,include
router = DefaultRouter()
# router.register('candiddates',CandidateViewSet,basename='candidate'),
router.register('project-description',ProjectDescriptionViewSet,basename='project-description'),
router.register('company',CompanyViewSet,basename='company'),
# router.register('project',ProjectViewSet,basename='project'),
router.register('team', TeamViewSet, basename='team'),
router.register('hobby', HobbyViewSet, basename='hobby'),
router.register('skill-description', SkillDescriptionViewSet, basename='skill-description'),
router.register('skill-title', SkillTitleViewSet, basename='skill-title'),
router.register('content', ContentViewSet, basename='content'),

# urlpatterns = [
#     path('project/',ProjectViewSet.as_view(), name='project'),       
# ]