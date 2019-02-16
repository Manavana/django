import json
from django.shortcuts import render
from products.models import product

# Create your views here.
def products(request):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)

    data = product.objects.all()

    return render(
        request,
        'products/products.html',
        {'object_list': data}
    )

def product_detail_view(request, pk):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)

    data = product.objects.get(pk=pk)

    return render(
        request,
        'products/detail.html',
        {'object': data}
    )