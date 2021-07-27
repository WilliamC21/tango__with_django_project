from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #dictionary used to pass into template as context()
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'} #boldmessage: mathces HTML doc name
   
    #returns rendered response, first parameter = desired template
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by William'}
    return render(request, 'rango/about.html', context=context_dict)