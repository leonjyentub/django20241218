from django.contrib.auth.models import AbstractUser
from django.db import models

# 在 mymessages/models.py 中
from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser (AbstractUser ):
    nickname = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)  # 新增生日字段
    address = models.CharField(max_length=255, blank=True)  # 新增地址字段^^
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # 新增照片字段

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]