from django.urls import path
from .views import login_view, register_view

app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('registration/', register_view, name='registration')
]
