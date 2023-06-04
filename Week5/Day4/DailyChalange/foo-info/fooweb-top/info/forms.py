from django import forms
from .models import Person


# class PersonForm(forms.ModelForm):
#     class Meta :  
#         model= Person
#         fields= 'name', 'phone_number'
        
class SearchForm(forms.Form):
    query = forms.CharField(max_length = 20)