import json
from django.shortcuts import render

# Create your views here.
def products(request):
    with open('products/fixtures/data/data.json') as file:
        data = json.load(file)

        return render(
            request,
            'products/products.html',
            {'object_list': data}
        )

def product_detail_view(request, idx):
    with open('products/fixtures/data/data.json') as file:
        data = json.load(file)

        return render(
            request,
            'products/detail.html',
            {'object': data[idx]}
        )