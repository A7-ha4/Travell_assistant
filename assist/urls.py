from django.contrib import admin
from django.urls import path
from .views import travel_assistant

urlpatterns = [
    path('', travel_assistant, name='assistant'),
]
