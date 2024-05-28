from django.shortcuts import render

def login_view(request):
    
    context = {
        'message': 'Hello World!'
    }
    
    return render(request, "templates/login.html", context)