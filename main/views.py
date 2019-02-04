from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # template = Template(
    #     'Hello {{ name }}'
    # )
    # context = Context({
    #     'name': 'Maria'
    # })
    template = get_template(
        'main/index.html'
    )

    context = {
        'name': 'Anton'
    }
    return HttpResponse(
        template.render(context)
    )
    # return render(
    #     request,
    #     'main/index.html'
    # )

def menuSections(request):
    rendered_page = render_to_string(
        'main/index.html',
        'main/contacts.html',
        {
            'menuSections': [
                'about us',
                'products',
                'stok',
                'news',
                'master class',
                'contacts',
            ]
        }
    )
    return HttpResponse(
        rendered_page
    )

# def contacts(request):
#     rendered_page = render_to_string(
#         'main/contacts.html',
#         {
#             'contacts': [
#                 'Контакт 1',
#                 'Контакт 2',
#                 'Контакт 3',
#             ]
#         }
#     )
#     return HttpResponse(
#         rendered_page
#     )

    # return render(
    #     request,
    #     'main/contacts.html'
    # )