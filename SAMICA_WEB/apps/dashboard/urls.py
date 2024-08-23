from django.urls import path
from .views import DashboardHomeView


urlpatterns = [
    path('dashboard/', DashboardHomeView, name='dashboard'),
    ]