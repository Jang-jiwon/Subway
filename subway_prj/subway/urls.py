from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.map),
    path('map/stationdetail/<str:id>/', views.detail.as_view()),
    path('map/stationdetail/<str:id>/<int:code>', views.detail.as_view()),
    path('map/test', views.test)
]
