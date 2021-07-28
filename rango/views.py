from typing import OrderedDict
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    #dictionary used to pass into template as context()
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
   
    #returns rendered response, first parameter = desired template
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by William'}
    return render(request, 'rango/about.html', context=context_dict)