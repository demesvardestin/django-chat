from django.shortcuts import render
from chat_messages.models import ChatMessage

def chat_messages_index(request):
    chat_messages = ChatMessage.objects.all()
    context = {
        'chat_messages': chat_messages
    }
    return render(request, 'chat_messages_index.html', context)

def chat_message_detail(request, pk):
    chat_message = ChatMessage.objects.get(pk=pk)
    context = {
        'chat_message': chat_message
    }
    return render(request, 'chat_message_detail.html', context)