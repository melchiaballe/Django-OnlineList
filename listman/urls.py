from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'listman'

urlpatterns = [
    path('accounts/login/', views.login_user, name = "login"),
    path('accounts/logout/', views.logout_user, name = "logout"),
    path('accounts/output/', views.process_login, name = "process"),
    path('accounts/register/', views.register_user, name = "register"),
    path('accounts/forgetpassword/', views.forget_pass, name = "forgetpass"),
    path('', views.index, name = "index"),
]