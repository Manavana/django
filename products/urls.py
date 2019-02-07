from django.urls import path

from .views import (
    products, product_detail_view
)

urlpatterns = [
    path('', products),
    path('<int:idx>', product_detail_view),
]