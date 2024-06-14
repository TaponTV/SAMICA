from django.shortcuts import render, get_object_or_404
from apps.accounts.usecases.UserApplication import UserApplication
from apps.accounts.adapters.user_repository import users_repository


def user_details_view(request) -> render:

    adapter = users_repository()
    DataAccess = UserApplication(adapter) 
    datalist = DataAccess.read_users()
    if datalist is []:
        context = {'Data': 'Not Found Users in DB'}
        return render(request, 'admin_templates/users_details_info.html', context)
    context = {'Data': datalist}
    return render(request, 'admin_templates/users_details_info.html', context)
