from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from .models import List
from django.contrib.auth.models import User

class UserRegForm(UserCreationForm):
    email = forms.EmailField()

    def CreateDefaultList(self, request):
        listName = "Default"
        Description = "This is a default user list"
        uname = self.cleaned_data.get('username')
        user = User.objects.get(username=uname)
        List.objects.create(title=listName, owner=user, description=Description)

class UserLoginForm(forms.Form):
    username = forms.CharField(label = "username",max_length=200)
    password = forms.CharField(label= "password", max_length=200)

    def auth(self, request):
        uname = self.cleaned_data.get('username')
        pword = self.cleaned_data.get('password')
        return authenticate(request, username=uname, password=pword)