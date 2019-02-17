from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=128)
    password = forms.CharField(
        required=True,
        max_length=72,
        widget=forms.widgets.PasswordInput()
    )