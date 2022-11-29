from django import forms
from .models import Lobby, Reply

class LobbyForm(forms.ModelForm):
    class Meta:
        model = Lobby
        fields = ['title', 'food_category', 'area', 'member_number', 'content', 'image']
        widgets = {
            'food_category': forms.RadioSelect(),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields=['text']
        
