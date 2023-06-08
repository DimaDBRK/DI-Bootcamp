from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Image


class RegisterForm(UserCreationForm):
          class Meta:
              model = User
              fields = ['username', 'first_name', 'last_name' ,'password1', 'password2']

class ImageForm(forms.ModelForm):
    
    class Meta:
        image = forms.ImageField(required = False)
        model = Image
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput(),}
        