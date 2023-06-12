from typing import Any, Dict
from django import forms
from .models import Book, BookReview

from django.forms import formset_factory 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = '__all__'
        


BookFormSet = forms.modelformset_factory(model = Book, form =BookForm, extra=1)

