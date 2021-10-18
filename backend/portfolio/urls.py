from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('portfolio/', views.portfolio),
    path('example/', views.example),
]
