from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from users.models import CustomUser
from chat_rooms.models import ChatRoom
from friendships.models import Friendship
from .forms import CustomUserCreationForm

def home(request):
    if request.user.id is not None:
        current_user = request.user
        users = CustomUser.objects.all()
        if len(ChatRoom.objects.filter(user_one=current_user.username)) > 0:
            chat_rooms = ChatRoom.objects.filter(user_one=current_user.username)
        elif len(ChatRoom.objects.filter(user_two=current_user.username)) > 0:
            chat_rooms = ChatRoom.objects.filter(user_two=current_user.username)
        else:
            chat_rooms = []
        
        friendship_obj = Friendship.objects.filter(created_by=current_user)
        if len(friendship_obj) == 0:
            friendship_obj = Friendship.objects.filter(created_for=current_user.pk)
        
        created_by = [friendship.created_by.pk for friendship in friendship_obj if friendship.created_by != current_user]
        created_for = [friendship.created_for for friendship in friendship_obj]
        friendships = created_by + created_for
    
        context = {
            "users": users,
            "current_user": current_user,
            "chat_rooms": chat_rooms,
            "friendships": friendships
        }
    else:
        context = {}
    
    return render(request, 'home.html', context)

def message(request):
    current_user = request.user
    user_one = request.GET.get('username', '')
    chat_room = ChatRoom(user_one=user_one,user_two=current_user.username)
    chat_room.save()
    
    return redirect('/chat_rooms/' + str(chat_room.pk))
    
def follow(request):
    current_user = request.user
    user_id = int(request.GET.get('user_id', ''))
    friendship = Friendship(created_by=current_user,created_for=user_id)
    friendship.save()
    return redirect('/users/home')

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
