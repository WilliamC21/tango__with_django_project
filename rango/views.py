from typing import OrderedDict
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    #dictionary used to pass into template as context()
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list
   
    #returns rendered response, first parameter = desired template
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by William'}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    #create a context dictionary(will be passed to html file)
    context_dict = {}

    try:
        #try to find category name slug with given name(prameter passed)
        category = Category.objects.get(slug=category_name_slug)

        #retrieve all pages associated
        pages = Page.objects.filter(category = category)
        
        #add these pages to the dictionary
        context_dict['pages'] = pages

        #this used to verify category exists
        context_dict['category'] = category
    except Category.DoesNotExist: #throw exception if no such category
        #avoid doing anything, disaply no category message
        context_dict['category'] = None
        context_dict['pages'] = None\
    
    return render(request, 'rango/category.html', context=context_dict)

