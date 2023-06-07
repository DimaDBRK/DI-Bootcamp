from django import forms
from .models import Category, Film, Director
from accounts.models import UserProfile

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