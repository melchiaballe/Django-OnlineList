from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
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

def save_post(sender, instance, created, **kwargs):
        if created:
            List.objects.create(title="Default", 
                owner=instance,
                description="This is a default user list")

post_save.connect(save_post, sender=User)