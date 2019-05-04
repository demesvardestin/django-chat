from django.conf.urls import url
from . import views

urlpatterns = [
    url('home/', views.home, name='home'),
    url('message/', views.message, name='message'),
    url('follow/', views.follow, name='follow'),
    url('signup/', views.SignUp.as_view(), name='signup'),
]