from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, LoginForm

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class LoginPageView(generic.View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


def logoutView(request):
    logout(request)
    return redirect('login')