from django import forms
from .models import Category, Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ('date_creation','has_been_done','date_completion')
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type':'date'})}
        
class DoneForm(forms.Form):
    isinstance = forms.ModelMultipleChoiceField(queryset=Todo.objects.all(),
                                                widget = forms.HiddenInput())
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'     
        # fields = ('has_been_done','')
        # widgets = {
        #            'has_been_done': forms.HiddenInput(), #like CSS
        # }
# Examples
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         # exclude = ('author','')
#         widgets = {
#             'author': forms.HiddenInput(),
#             'content': forms.Textarea(attrs ={'row':5, 
#                                               'class': 'content_class'}), #like CSS
#         }
        

# class SearchForm(forms.Form):
#     query = forms.CharField(max_length = 20)