from django.urls import path
from .views import user_details_view, register_user_view

urlpatterns = [
    path('accounts/users', user_details_view, name='usersinfo'),
    path('accounts/register', register_user_view, name='registeruser')
]