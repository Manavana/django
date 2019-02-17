from django import forms
from .models import accountUser

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=128)
    password = forms.CharField(
        required=True,
        max_length=72,
        widget=forms.widgets.PasswordInput()
    )

class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(
        required=True,
        max_length=72,
        widget=forms.widgets.PasswordInput()
    )

    def clear_password_confirm(self):
        pass

    class Meta:
        model = accountUser
        fields = ['username', 'password']
