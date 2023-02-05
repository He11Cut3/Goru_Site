from django.shortcuts import render

from django.template.defaulttags import url
from django.urls import path
from app import views
from authentication import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path("logout/", views.logout_user, name='logout'),
]