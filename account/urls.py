from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('verify/', views.verify, name='verify'),
    ]
