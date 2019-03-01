from rest_framework.serializers import ModelSerializer

from products.models import category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = category
        fields = ['url', 'id', 'name']