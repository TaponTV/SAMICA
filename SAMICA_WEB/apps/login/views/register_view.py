from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.register_form import RegisterUserForm


def RegisterUserView(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('dashboard')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})