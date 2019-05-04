from django.conf.urls import url
from chat_rooms import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.chat_room_detail, name="chat_room_detail"),
]