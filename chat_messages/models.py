from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from chat_rooms.models import ChatRoom
from users.models import CustomUser

class ChatMessage(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)
    chat_room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, default=2)