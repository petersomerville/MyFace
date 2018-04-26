from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=32)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Following(models.Model):

    follower = models.ForeignKey(User, related_name='is_following', on_delete=models.CASCADE, default=0)
    following = models.ForeignKey(User, related_name='followed_by', on_delete=models.CASCADE, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Photo(models.Model):
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)