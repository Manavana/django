from django.urls import path
from .views import login_view, register_view, AccountRegistrationView, AccountLoginView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('', AccountLoginView.as_view(), name='login'),
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout')
]
