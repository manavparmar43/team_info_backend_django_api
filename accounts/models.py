from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


from profile.models import Team

## login user roles
class UserRole(DateTimeMixin):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    admin = models.BooleanField(default=False)
    access_team = models.ManyToManyField(Team, blank=True)
    access_accept = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.user)

from rest_framework.authtoken.models import Token

class NonBuiltInUserToken(Token):
   
    user = models.ForeignKey(
        User, related_name='auth_token',
        on_delete=models.CASCADE, 
    )

