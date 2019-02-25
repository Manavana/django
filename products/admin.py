from django.contrib import admin
from .models import product, category
from django.template.loader import render_to_string

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'picture', 'category', 'price', 'modified', 'created', 'is_new'
    ]

    list_filter = [
        'category', 'modified', 'created',
    ]

    search_fields = [
        'name', 'description'
    ]

    fieldsets = (
        (
            None, {
                'fields': ('name', 'category')
            },
        ),
        (
            'Content', {
                'fields': ('image', 'description', 'price')
            },
        ),
    )

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {
                'image': obj.image
            }
        )


    def is_new(self, obj):
        return obj.modified == obj.created


class ProductInline(admin.TabularInline):
    model = product


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'modified', 'created'
    ]

    list_filter = [
        'modified', 'created',
    ]

    search_fields = [
        'name', 'description'
    ]

    inlines = [
        ProductInline
    ]


admin.site.register(product, ProductAdmin)
admin.site.register(category, CategoryAdmin)