from django.forms import ModelForm
from .models import Game, System, XPL, GameStyle

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'gm_required', 'system', 'experience_lvl', 'players', 'game_style', 'about']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['system'].queryset = System.objects.none()
            self.fields['experience_lvl'].queryset = XPL.objects.none()
            self.fields['game_style'].queryset = GameStyle.objects.none()

            if 'system' in self.data:
                self.fields['system'].queryset = System.objects.all() 

            if 'experience_lvl' in self.data:
                self.fields['system'].queryset = XPL.objects.all() 

            if 'game_style' in self.data:
                self.fields['system'].queryset = GameStyle.objects.all() 

class GameDeleteForm(ModelForm):
    class Meta:
        model = Game
        fields = []