from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def DashboardHomeView(request):
    context = {
        'title': 'Dashboard',
        'message': 'Bienvenido al dashboard'
    }
    
    return render(request, 'dashboard.html', context)
    