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

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')

    class Meta:
        model = accountUser
        fields = ['username', 'password']
