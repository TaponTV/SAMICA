from django.urls import path
from .views import LogInUserView

urlpatterns = [
    path('', LogInUserView, name='login'),
    
]
