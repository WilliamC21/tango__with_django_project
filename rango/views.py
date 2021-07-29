from rango.forms import CategoryForm, PageForm
from typing import OrderedDict
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from rango.models import Category, Page
from django.urls import reverse

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

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        
        else: print (form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
            else:
                print(form.error)

        context_dict = {'form' : form, 'category': category}
        return render(request, 'rango/add_page.html', context = context_dict)
