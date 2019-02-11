from django.forms import forms

class categoryForm(forms.Form):
    name = forms.CharField(required=True)

    description = forms.CharField(
        widget=forms.widgets.Textarea()
    )