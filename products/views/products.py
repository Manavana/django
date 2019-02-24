import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products.models import product
from products.forms import productForm
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.core.paginator import Paginator

class ProductListView(ListView):
    model = product
    template_name = 'products/products.html'
    paginate_by = 3

    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     queryset = context.get('object_list')
    #
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(queryset, 3)
    #     page_obj = paginator.get_page(page)
    #
    #     context['page_obj'] = page_obj
    #
    #     return context

class ProductDetailView(DetailView):
    model = product
    template_name = 'products/detail.html'

class ProductCreateView(CreateView):
    model = product
    form_class = productForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')

class ProductUpdateView(UpdateView):
    model = product
    fields = [
        'name', 'image', 'category', 'description', 'price'
    ]
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:list')

class ProductDeleteView(DeleteView):
    model = product
    template_name = 'products/delete.html'

def products(request):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)

    data = product.objects.all()

    return render(
        request,
        'products/categories.html',
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
    success_url = reverse('products:list')

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(
        request,
        'products/delete.html',
        {'object': obj}
    )