from django import forms
from .models import Home

class AdvertForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['title', 'description', 'price', 'location', 'category', 'image', 'additional_photos']
