from django.forms import ModelForm
from .models import Game

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title']

class GameDeleteForm(ModelForm):
    class Meta:
        model = Game
        fields = []