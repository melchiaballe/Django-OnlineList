from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login, logout

class UserRegForm(UserCreationForm):
    email = forms.EmailField()


class UserLoginForm(forms.Form):
    username = forms.CharField(label = "username",max_length=200)
    password = forms.CharField(label= "password", max_length=200)

    def auth(self, request):
        uname = self.cleaned_data.get('username')
        pword = self.cleaned_data.get('password')
        return authenticate(request, username=uname, password=pword)