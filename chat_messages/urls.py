from django.conf.urls import url
from . import views

urlpatterns = [
    url("", views.chat_messages_index, name="chat_messages_index"),
    url("<int:pk>/", views.chat_message_detail, name="chat_message_detail"),
]