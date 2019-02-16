from django import forms
from products.models import product

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'image', 'category', 'description', 'price']