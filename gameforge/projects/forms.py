from django import forms
from .models import GameProject

class GameProjectForm(forms.ModelForm):
    class Meta:
        model = GameProject
        fields = ['title', 'genre', 'ambiance', 'keywords']
