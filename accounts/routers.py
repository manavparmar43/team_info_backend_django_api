
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenVerifyView
)
routers = DefaultRouter()
routers.register('active-user-role',ActiveUserrole,basename='active-user-role'),
routers.register('list-team',TeamListViewset,basename='list-team'),
routers.register('user-list',UserListViewSet,basename='user-list'),
routers.register('user-role',UserRoleApiViewset,basename='user-role'),
# routers.register('candidate',TeamCandidateListViewSet,basename='candidate'),
urlpatterns = [
    path('login/',LoginView.as_view(), name='login'),       
    # path('userrole/', UserRoleApiView.as_view(), name='userrole'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-create/', UserApiView.as_view(), name='user-create'),

    path('verify-token/', TokenVerifyView.as_view(), name='verify-token'),
]
