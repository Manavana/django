from django.urls import path

from products.views import (
    category_create_view, category_update_view
)

urlpatterns = [
    path('create/', category_create_view, name='create'),
    path('<int:pk>/update/', category_update_view, name='update'),
]