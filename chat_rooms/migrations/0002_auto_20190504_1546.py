# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-04 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='user_one',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='user_two',
            field=models.CharField(default='', max_length=255),
        ),
    ]