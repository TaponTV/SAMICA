from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.get_user_data import get_user_data
from ..usecases import GetDashboardButtons



@login_required
def DashboardHomeView(request):
    auth_user = request.user
    context = get_user_data(auth_user)
    context['academic'] = auth_user.academic_key
    context['buttons'] =  GetDashboardButtons().execute()
    return render(request, 'dashboard.html', context)
    
