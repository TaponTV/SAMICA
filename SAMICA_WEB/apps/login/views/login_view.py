from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.login_form import LogInUserForm


def LogInUserView(request):
    if request.method == 'POST':
        form = LogInUserForm(request.POST)
        if form.is_valid():
            auth_user = form.get_user()
            login(request, auth_user)
            return redirect('dashboard')
    else:
        form = LogInUserForm()
    return render(request, "login.html", {'form': form})
