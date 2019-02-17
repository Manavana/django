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
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password is not confirm')

        return self.cleaned_data

    class Meta:
        model = accountUser
        fields = ['username', 'password']
