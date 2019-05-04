from __future__ import unicode_literals
from django.db import models

class ChatRoom(models.Model):
    description = models.TextField()
    user_one = models.CharField(max_length=255,default="")
    user_two = models.CharField(max_length=255,default="")