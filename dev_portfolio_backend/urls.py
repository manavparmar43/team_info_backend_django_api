"""dev_portfolio_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profile.routers import router
# from profile.routers import *
from accounts.routers import routers
from profile.views import UserCreate

urlpatterns = [
    path('api/',include(router.urls)),
    path('profile/',include('profile.urls')),
    path('account/',include(routers.urls)),
    path('',include('accounts.routers')),
    path('admin/', admin.site.urls),
    path('create-user', UserCreate.as_view(), name='create'),
    
    # path("", include('admin_volt.urls'))
]
