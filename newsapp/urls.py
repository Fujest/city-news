from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('<slug:slug>/', tagged, name='tagged')
]
