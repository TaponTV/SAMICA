from django.urls import path
from .views import user_details_view

urlpatterns = [
    path('accounts/users', user_details_view, name='usersinfo')
]