from django import forms
from products.models import category

class categoryForm(forms.Form):
    name = forms.CharField(required=True)

    description = forms.CharField(
        widget=forms.widgets.Textarea()
    )

class categoryModelForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name', 'description']