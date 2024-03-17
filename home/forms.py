from django import forms
from .models import Home
from .models import Message

class AdvertForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['title', 'description', 'price', 'location', 'category', 'image', 'additional_photos']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject','message']
