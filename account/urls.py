from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('verify/', views.verify, name='verify'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('change_password/', views.change_password, name='change_password'),
    ]
