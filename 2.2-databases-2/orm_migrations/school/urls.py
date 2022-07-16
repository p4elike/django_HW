from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from .views import students_list

urlpatterns = [
    path('', students_list, name='students'),

]

