from django import forms
from .models import Category, Film, Director, Review
from django.forms import RadioSelect

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        

class ReviewForm(forms.ModelForm):
    
    rating = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], widget=RadioSelect)
    
    class Meta:
        model = Review
        fields = '__all__'