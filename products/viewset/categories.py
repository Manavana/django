from rest_framework.viewsets import ModelViewSet

from products.models import category

from products.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer