from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=200)
    lst = models.ForeignKey(List, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title