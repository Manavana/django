from django.urls import path

from .views import (
    index, contacts
)

urlpatterns = [
    path('', index, name='main'),
    path('contacts/', contacts),
]