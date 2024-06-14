from django import forms
from apps.accounts.models import Users
from django.contrib.auth.hashers import make_password


class RegisterUserForm(forms.ModelForm):

    password_in = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password_match = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'academic_key']

    def clean_password2(self):
        pass1 = self.cleaned_data['password_in']
        pass2 = self.cleaned_data['password_match']
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('Las contraseñas no coinciden, por favor intentelo de nuevo')
        return pass2

    def save(self, commit=True):
        new_user = super().save(commit=False)
        new_user.password = make_password(self.cleaned_data["password_in"])
        if commit:
            new_user.save()
        return new_user