from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.map),
    path('map/stationdetail', views.detail.as_view()),
    path('map/test', views.test)
]
