from django.urls import path

from .views import (
    index, contacts
)

app_name = 'main'

urlpatterns = [
    path('', index, name='main'),
    path('contacts/', contacts),
]