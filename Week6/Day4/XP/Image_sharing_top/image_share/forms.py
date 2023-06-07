from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image


class RegisterForm(UserCreationForm):
          class Meta:
              model = User
              fields = ['username', 'first_name', 'last_name' ,'password1', 'password2']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        # exclude = ('author','')
        # widgets = {
        #     'author': forms.HiddenInput(),
        #     'content': forms.Textarea(attrs ={'row':5, 
        #                                       'class': 'content_class'}), #like CSS
        # }