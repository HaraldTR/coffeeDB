"""coffeedb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from django.conf import settings

from coffeeApp.urls import get_user_coffee_app_router, get_backend_coffee_app_router

user_coffee_app_router = get_user_coffee_app_router()
backend_coffee_app_router = get_backend_coffee_app_router()

urlpatterns = [
    path("user/", include(user_coffee_app_router.urls)),
    path("backend/", include(backend_coffee_app_router.urls)),
    path("admin/", admin.site.urls),
]