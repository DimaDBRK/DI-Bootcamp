from django import forms
from .models import Category, Gif #import the Post model from polls/models.py
from django.forms import ModelMultipleChoiceField
from django.forms import ModelForm


# uploader_name
# title
# url : You can use the gifs’ url from the giphy website. Click on the gif you want, and copy the gif link.
# categories : look up ModelMultipleChoiceField

class GifForm(ModelForm):
       
    uploader_name = forms.CharField(label = 'uploader_name')
    title = forms.CharField(label = 'title')
    url = forms.URLField()
    
    # name = forms.ModelMultipleChoiceField(queryset = Category.objects.all(), label="Category", widget=forms.CheckboxSelectMultiple, required=False) #look up ModelMultipleChoiceField
    
    class Meta:
        model = Gif
        exclude = ['created_at']
        # fields = '__all__'
        # model = Category
        # exclude = ['gifs']
           
# name           
class CategoryForm(ModelForm):
    name = forms.CharField(label = 'Category name')
    # gifs = forms.ModelMultipleChoiceField(queryset = Gif.objects.all().order_by('title'), label="Category", widget=forms.CheckboxSelectMultiple, required=False) #look up ModelMultipleChoiceField
    
    class Meta:
        model = Category
        # exclude = ['id']
        fields = '__all__'
       
      