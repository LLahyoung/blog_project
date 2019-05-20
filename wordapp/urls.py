from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('detail/', views.worddetail, name="worddetail"),
    path('result/', views.wordresult, name="wordresult"),
    path('home/', views.wordhome, name="wordhome"),

]