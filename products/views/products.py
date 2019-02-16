import json
from django.shortcuts import render, redirect
from products.models import product, category
from products.forms import categoryForm, categoryModelForm
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

# def category_create_view(request):
#     form = categoryForm()
#     success_url = reverse('list')
#
#     if request.method == 'POST':
#         form = categoryForm(data=request.POST)
#         if form.is_valid():
#             obj = category(
#                 name=form.cleaned_data.get('name'),
#                 description=form.cleaned_data.get('description')
#             )
#
#         obj.save()
#
#         return redirect(success_url)
#
#     return render(
#         request,
#         'categories/create.html',
#         {'form': form}
#     )

def category_create_view(request):
    form = categoryModelForm()
    success_url = reverse('list')

    if request.method == 'POST':
        form = categoryModelForm(data=request.POST)

        if form.is_valid():
            form.save()
            # obj = category(
            #     name=form.cleaned_data.get('name'),
            #     description=form.cleaned_data.get('description')
            # )
            #
            # obj.save()

        return redirect(success_url)

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )

def category_update_view(request, pk):
    try:
        obj = category.objects.get(pk=pk)
    except Exception as err:
        raise Http404

    form = categoryModelForm(instance=obj)
    success_url = reverse('list')
    if request.method == 'POST':
        form = categoryModelForm(
            request.POST,
            files=request.FILES,
            initial=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'categories/update.html',
        {'form': form}
    )