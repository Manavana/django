import json
from django.shortcuts import render, redirect
from products.models import category
from products.forms import categoryForm, categoryModelForm
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class CategoryListView(ListView):
    model = category
    template_name = 'categories/categories.html'

class CategoryDetailView(DetailView):
    model = category
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        key = self.context_object_name if self.context_object_name else 'object'
        obj = kwargs.get(key)
        products = obj.product_set.all()

        return {
            key: obj,
            'products': products
        }

class CategoryCreateView(CreateView):
    model = category
    form_class = categoryModelForm
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:list')

class CategoryUpdateView(UpdateView):
    model = category
    form_class = categoryModelForm
    template_name = 'categories/update.html'
    success_url = reverse_lazy('categories:list')

class CategoryDeleteView(DeleteView):
    model = category
    template_name = 'categories/delete.html'

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
    success_url = reverse('products:list')

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
    success_url = reverse('products:list')
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