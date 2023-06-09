from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.map),
    path('map/stationdetail/<str:id>/', views.detail.as_view()),
    path('map/stationdetail/<str:id>/<int:code>', views.detail.as_view()),
    path('map/route', views.route),
    path('map/test', views.test),

    path('map/searchId/<str:q>/', views.SearchId),
    path('map/searchStation/<str:id>/', views.SearchStation),
    path('map/cgPredict/<int:id>/<int:day>/', views.cgPredict),
]
