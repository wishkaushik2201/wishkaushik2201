"""Libraryapp URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('mybook/',views.mybook ,name='mybook'),
    path('subscription/',views.subscription ,name='subscription'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('login/',views.login,name='login'),
    path("login_in",views.login_in,name='login_in'),
    path('signup',views.signup ,name='signup'),
    path('reg/',views.reg ,name='reg'),
]
