import json
from django.shortcuts import render
from .models import product, category
from .forms import categoryForm

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

def category_create_view(request):
    form = categoryForm()

    if request.method == 'POST':
        obj = category(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )

        obj.save()

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )
