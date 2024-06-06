from django.urls import path
from .views import *

urlpatterns = [
    path('', LogInUserView, name='login'),
    path('signup/', RegisterUserView, name='signup')
    
]
