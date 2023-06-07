from typing import Any, Dict
from django import forms
from .models import Category, Film, Director, Producer
from accounts.models import UserProfile
from django.forms import formset_factory 

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        

# class FavouriteFilmForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
        # exclude = ('author','')
        # widgets = {
        #     'author': forms.HiddenInput(),
        #     'content': forms.Textarea(attrs ={'row':5, 
        #                                       'class': 'content_class'}), #like CSS
        # }
        
class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'


ProducerFormSet = forms.modelformset_factory(model = Producer, form = ProducerForm, extra=1)

