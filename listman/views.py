from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from .forms import UserRegForm, UserLoginForm, UpdateUser
from .models import List, Todo
from django.urls import reverse

# Create your views here.

def update_index_content(request, id):
    if request.user.is_authenticated:
        form = List.objects.filter(owner = request.user)
        listform = List.objects.filter(pk = id)
        return render(request, 'listman/base.html', {'form':form, 'listform':listform})
    else:
        return redirect('listman:login')
    
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
    
def process_add_list(request):
    if request.user.is_authenticated:
        listname = request.POST.get('listname')
        listnamecontent = List.objects.filter(owner = request.user)
        if listname is not '' and listname not in listnamecontent:
            List.objects.create(title = listname, owner = request.user)
        
        return redirect('listman:index')
    else:
        return redirect('listman:login')

def edit_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateUser(request.POST)
            if form.is_valid():
                form.update(request)
                return redirect('listman:index')
            else:
                form = UpdateUser(request.POST)
        else:
            form = UpdateUser(request.POST)
        return render(request, 'listman/edit_user.html', {'form':form})
    else:
        return redirect('listman:login')

def edit_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('listman:logout')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'listman/edit_password.html', {'form': form})
    else:
        return redirect('listman:login')


def process_delete_list(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            lst = get_object_or_404(List, id=id, owner=request.user)
            lst.delete()
            return redirect('listman:index')
        else:
            return redirect('listman:index')
    else:
        return redirect('listman:login')

def add_list_todos(request, id):
    if request.user.is_authenticated:
        return HttpResponse("SUCCESS")
    else:
        return redirect('listman:login')
