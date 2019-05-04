from __future__ import unicode_literals
from django.db import models
from users.models import CustomUser

class Friendship(models.Model):
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    created_for = models.IntegerField(default=2)
    currently_active = models.BooleanField(default=True)