from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegForm, UserLoginForm
from .models import List, Todo
from django.urls import reverse

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        form = List.objects.filter(owner = request.user)
        return render(request, 'listman/base.html', {'form':form})
    else:
        return redirect('listman:login')
    

def login_user(request):
    return render(request, 'listman/login.html')

def logout_user(request):
    logout(request)
    return redirect('listman:login')


def process_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.auth(request)
            if user is not None:
                login(request, user)
                return redirect('listman:index')
            else:
                form.add_error(None, "Invalid Entry")
        else:
            form = UserLoginForm(request.POST)
            form.add_error(None, "Invalid Entry")
        return render(request, 'listman/login.html', {'form':form})

def register_user(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')
            user.save()
            form.CreateDefaultList(request)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('listman:index')
        else:
            form = UserRegForm(request.POST)
    else:
        form = UserRegForm()
    return render(request, 'listman/register.html', {'form': form})

def forget_pass(request):
    return render(request, 'listman/reset_password.html')
    


