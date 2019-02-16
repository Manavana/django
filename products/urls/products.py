from django.urls import path

from products.views import (
    products, product_detail_view
)

app_name = 'products'

urlpatterns = [
    path('', products, name='list'),
    path('<int:pk>/', product_detail_view, name='detail'),
]