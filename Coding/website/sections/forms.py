from django import forms

from .models import news

class addingnews(forms.ModelForm):
    class Meta:
        model = news
        fields = [
            'title',
            'paragraph',
            'paragraph2',
            'image',
        ]