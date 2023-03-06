from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from profile.serializers import *
# from cryptography.fernet import Fernet
# import cryptocode
import base64
# key = Fernet.generate_key()
# fernet = Fernet(key)
# from cryptography.fernet import Fernet
import jwt
from django.conf import settings

class MyTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['is_superuser']=self.user.is_superuser
        return data

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','first_name','last_name' ]
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data["password"] = make_password(password)
        email = validated_data.pop('email')
        validated_data["email"] = jwt.encode(
            {"email": email},
            settings.ENCRYPT_SECURITY_KEY,
            algorithm="HS256",
        )
        instance = super().create(validated_data)
        instance.save()
        return instance    


class ActiveTeamSerializer(DynamicFieldsModelSerializer):
    # team_key=CandidateListSerializer(many=True,read_only=True)
    access_team=TeamSerializer(many=True,read_only=True)
    #   user=UserSerializer(fields = ['username'],many=True,read_only=True)
    class Meta:
          model=UserRole
          fields = ['id','name','access_team']
      


    