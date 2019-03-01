from rest_framework.serializers import ModelSerializer, SerializerMethodField

from products.models import product


class ProductSerializer(ModelSerializer):

    category = SerializerMethodField()
    is_new = SerializerMethodField()

    class Meta:
        model = product
        fields = ['url', 'id', 'name', 'category', 'image', 'price', 'is_new']

    def get_category(self, obj):
        if obj.category:
            return obj.category.name

    def get_is_new(self, obj):
        return obj.created == obj.modified