from django import forms

class ChatMessageForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Type your message...",
            "id": "chat-message-content",
            "onkeyup": "submitForm(event)"
        })
    )