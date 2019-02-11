from django.urls import path

from .views import (
    products, product_detail_view, category_create_view, category_update_view
)

urlpatterns = [
    path('', products, name='list'),
    path('<int:pk>/', product_detail_view, name='detail'),
    path('categories/create/', category_create_view, name='create'),
    path('categories/<int:pk>/update/', category_update_view, name='update'),
]