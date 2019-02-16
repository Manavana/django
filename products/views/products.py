import json
from django.shortcuts import render, redirect, get_object_or_404
from products.models import product
from products.forms import productForm
from django.urls import reverse
from django.http import Http404

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

def product_create_view(request):
    form = productForm()
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = productForm(data=request.POST)

        if form.is_valid():
            form.save()

        return redirect(success_url)

    return render(
        request,
        'products/create.html',
        {'form': form}
    )

def product_update_view(request, pk):
    obj = get_object_or_404(product, pk=pk)

    form = productForm(instance=obj)
    success_url = reverse('products:list')
    if request.method == 'POST':
        form = productForm(
            request.POST,
            files=request.FILES,
            initial=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/update.html',
        {'form': form}
    )

def product_delete_view(request, pk):
    obj = get_object_or_404(product, pk=pk)

    return render(
        request,
        'products/delete.html',
        {'object': obj}
    )