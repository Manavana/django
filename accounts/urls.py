from django.urls import path
from .views import login_view, register_view, RegistrationView
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration')
]
