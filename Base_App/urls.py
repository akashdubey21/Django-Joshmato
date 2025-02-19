from django.contrib import admin
from django.urls import path,include
from Base_App.views import Home_view

urlpatterns = [
    path('', Home_view,name="Home_view"),
    
]