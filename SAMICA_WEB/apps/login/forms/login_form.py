from typing import Any
from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class LogInUserForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        try:
            auth_user = User.objects.get(username=username)
            if not auth_user.check_password(password):
                raise forms.ValidationError("Contraseña inválida")
        except User.DoesNotExist:
            raise forms.ValidationError("Usuario inválido")
        
        return self.cleaned_data
    
    def get_user(self):
        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)