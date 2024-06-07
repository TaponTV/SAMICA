from django.shortcuts import render, get_object_or_404
from apps.accounts.usecases.users_info import GetUserInfo

def user_details_view(request) -> render:
    
    instance = GetUserInfo()
    if instance is []:
        context = {'Data': 'Not Found Users in DB'}
        return render(request,'admin_templates/users_details_info.html', context)
    context = {'Data': instance.ListObject}
    return render(request, 'admin_templates/users_details_info.html', context)
    