from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from profile.serializers import TeamSerializer
from profile.models import *
from rest_framework.response import Response 
from .serializers import (
    UserRoleSerializer,
    UserSerializer,
    MyTokenObtainPairSerializer,
#    key,fernet
)
# import cryptocode
from rest_framework.generics import CreateAPIView
from profile.serializers import * 
from rest_framework.views import APIView

from django.http import JsonResponse
from rest_framework import viewsets
import base64,json
# from cryptography.fernet import Fernet
from rest_framework_simplejwt.views import TokenObtainPairView
import jwt
from django.conf import settings


class UserApiView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class UserListViewSet(viewsets.ViewSet):
    def list(self,request):
        # if request.user.is_superuser:
            
            user=User.objects.all()
            lst=[]
            for i in user:
                dict={}
                dict['id']=i.id
                dict['first_name']=i.first_name
                dict['last_name']=i.last_name
                dict['username']=i.username
                dict['password']=i.password

                try:
                    decrypted_email = jwt.decode(
                    i.email, settings.ENCRYPT_SECURITY_KEY, algorithms=["HS256"]
                    )
                    dict["email"]=decrypted_email
                except:
                    dict["email"]=i.email

                lst.append(dict)
            return Response(lst)
        # else:
        #     return JsonResponse({"Error":"only admin can show data"})
class UserRoleApiViewset(viewsets.ViewSet):
    def create(self, request):
        user=User.objects.filter(username=request.user.username)
        if user:
            userrole_dict={
                "user":request.user.id,
                "name":request.user.first_name +' '+request.user.last_name ,
                "access_team":request.data.get('access_team')
            }
            serializer=UserRoleSerializer(data=userrole_dict)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"Success":serializer.data})
            else:
                return JsonResponse({"Error":"Userrole not create"})
        else:
            return JsonResponse({"Error":"User not found"})
    def list(self, request):
        user=User.objects.filter(username=request.user.username)
        if user:
            queryset=UserRole.objects.get(user=request.user.id,access_accept=True)
            lst=[]
            err_lst=[]
            if queryset:
                for j in queryset.access_team.values():
                        team_data=Team.objects.get(id=j['id'])
                        candidate_data=Candidate.objects.filter(team_key=team_data)
                        serializer=CandidateListSerializer(candidate_data,many=True)
                        if candidate_data:
                            lst.append(serializer.data)
                return JsonResponse({"Data":lst})
            else:
                return JsonResponse({"Error":"No Any Team access permission"})
        else:
            return JsonResponse({"Error":"Please Create user after you can get list of team permission"})


        



        
class TeamListViewset(viewsets.ViewSet):
    def list(self, request):
        if User.objects.filter(username=request.user.username).exists():
            queryset=Team.objects.all()
            if queryset:
                serializer = TeamSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return JsonResponse({"Error":"No Any Team "})
        else:
            return JsonResponse({"Error":"Create User after you can show the team"})

# class UserRoleApiView(APIView):
#     def post(self,request):
#         user_data_dict={
#                         'username':request.data.get('username'),
#                         'password':request.data.get('password'),
#                         'email':request.data.get('email')
#                         }
#         serializer=UserSerializer(data=user_data_dict)
#         if serializer.is_valid():
#             serializer.save()
#             user_data=User.objects.get(username=serializer.data['username'])
#             userrole_data_dict={
#                                 'user':user_data.id,
#                                 'name':request.data.get('name'),
#                                 'access_team':request.data.get('access_team')
#                                }  
#             serializer=UserRoleSerializer(data=userrole_data_dict)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({"Success":serializer.data})
#             else:
#                 return JsonResponse({"error":serializer.errors })
#         else:
#             return JsonResponse({"error":serializer.errors })

class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


        
        

class ActiveUserrole(viewsets.ViewSet):  
    def list(self, request):
        if request.user.is_superuser:
            queryset = UserRole.objects.all()
            serializer = UserRoleSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return JsonResponse({"Error":"Only Admin can Access"})
        
    def partial_update(self, request, pk=None):
        if request.user.is_superuser:
            instance = UserRole.objects.get(pk=pk)
            serializer = UserRoleSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)         
        else:
            return JsonResponse({"Error":"only admin can allow "})


class LogoutView(APIView):  
    def get(self, request):
        logout(request)
        return Response('logout done')



# Create your views here.
# def Token_Require(request):
#     try:
#         token_data = request.headers.get('Authorization')
#         token = token_data.split(" ")[1]
#         if token:
#             token_1 = decode_token(token)
#             print(token_1)
#             return token_1
#     except:
#         return Response("Auth Token not found")
    



    
        

# class UserDetailView(APIView):
#     def get(self, request):
#         data = Token_Require(request)
#         data1 = User.objects.get(id=data['user'])
#         return Response('Successfully retrieved')

