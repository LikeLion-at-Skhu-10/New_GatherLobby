from django import forms
from .models import Lobby, Reply

class LobbyForm(forms.ModelForm):
    class Meta:
        model = Lobby
        fields = ['title', 'area', 'member_number', 'content', 'image']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields=['text']
        
