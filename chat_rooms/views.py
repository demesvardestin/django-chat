from django.shortcuts import render
from chat_rooms.models import ChatRoom
from chat_messages.models import ChatMessage
from chat_messages.forms import ChatMessageForm
from users.models import CustomUser

def chat_room_detail(request, pk, content=None):
    current_user = request.user
    chat_rooms = ChatRoom.objects.all()
    chat_room = ChatRoom.objects.get(pk=pk)
    chat_room_messages = ChatMessage.objects.filter(chat_room=chat_room)
    form = ChatMessageForm()
    
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = ChatMessage(
                content=content or form.cleaned_data["content"],
                chat_room=chat_room,
                user = current_user
            )
            message.save()
    
    context = {
        'chat_room': chat_room,
        "chat_rooms": chat_rooms,
        'chat_room_messages': chat_room_messages,
        'form': form,
        'current_user': current_user
    }
    return render(request, 'chat_room_detail.html', context)