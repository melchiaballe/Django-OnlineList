from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'listman'

urlpatterns = [
    path('', views.index, name = "index"),
    path('accounts/login/', views.login_user, name = "login"),
    path('accounts/logout/', views.logout_user, name = "logout"),
    path('accounts/output/', views.process_login, name = "process"),
    path('accounts/register/', views.register_user, name = "register"),
    path('accounts/edit/user', views.edit_user, name = "edit"),
    path('accounts/edit/password', views.edit_password, name = "editpass"),
    path('accounts/forgetpassword/', views.forget_pass, name = "forgetpass"),
    path('list/add', views.process_add_list, name = "addlist"),
    path('list/<int:id>', views.update_index_content, name = "labelPress"),
    path('list/delete/<int:id>', views.process_delete_list, name = "deletelist"),
    path('list/add/<int:id>/todo', views.add_list_todos, name = "addtodo"),
]