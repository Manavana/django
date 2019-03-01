from rest_framework.viewsets import ModelViewSet

from products.models import product
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer