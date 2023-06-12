from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView
from .forms import RegisterForm


from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    
    

@login_required
def profile(request, id):
  user = User.objects.get(id=id)
  return render(request, 'profile.html', {'user': user})
