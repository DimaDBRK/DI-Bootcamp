from typing import Any, Dict
from django import forms
from .models import Book, BookReview

from django.forms import formset_factory 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
# class BookReviewForm(forms.ModelForm):
#     class Meta:
#         model = BookReview
#         fields = '__all__'
        


# BookFormSet = forms.modelformset_factory(model = Book, form =BookForm, extra=1)

class BookReviewForm(forms.ModelForm):
    
    raiting = forms.ChoiceField(label="Your rating",  choices=(('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')),initial='5', widget=forms.RadioSelect(attrs={'class': 'inline'}))

    class Meta:
        model = BookReview
        fields = ['user', 'book','review','raiting']
        RATING_CHOICES=(('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five'))
        widgets = {
            'user': forms.HiddenInput(),
            'book': forms.HiddenInput(),
            }