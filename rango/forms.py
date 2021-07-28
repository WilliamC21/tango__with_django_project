from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms:CharField(max_length=128,
                            help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) #even tho these are 
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0) #hidden still need to declare
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category #associate form and model
        fields = ('name',)

class PageForm(forms.ModelForm):

        title = forms.CharField(max_length = 128,
                                help_text="Please enter the title of the page.")
        url = forms.URLField(max_length =200,
                                help_text='Please enter the URL of the page'.)
        views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        
        class Meta:
            model = Page
            exclude = ('category')