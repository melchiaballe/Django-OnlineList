from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from .models import List
from django.contrib.auth.models import User

class UserRegForm(UserCreationForm):
    email = forms.EmailField()

    def save(self):
        super().save(self.username, self.password1, self.password2)

class UserLoginForm(forms.Form):
    username = forms.CharField(label = "username",max_length=200)
    password = forms.CharField(label= "password", max_length=200)

    def auth(self, request):
        uname = self.cleaned_data.get('username')
        pword = self.cleaned_data.get('password')
        return authenticate(request, username=uname, password=pword)

class UpdateUser(forms.Form):
    username = forms.CharField(max_length=200, required=False)
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(required=False)

    def update(self, request):
        uname = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        User.objects.filter(pk=request.user.id).update(username=uname, email=email, first_name=first_name, last_name=last_name)
