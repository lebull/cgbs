from django import forms
from models import Pick, Game

        
class PickForm(forms.ModelForm):
    
    class Meta:
        model = Pick
        fields = ('game', 'winner', 'funny_winner_name', 'funny_looser_name')
    
    def __init__(self, *args, **kwargs):
        if 'game' in kwargs:
            game = kwargs.pop('game')
            super(PickForm, self).__init__(*args, **kwargs)
            
            choices = [(game.away_team.id, game.away_team), (game.home_team.id, game.home_team)]
            self.fields['winner'].widget = forms.RadioSelect(choices=choices)
            self.fields['game'].widget = forms.HiddenInput(attrs={'value':game.id})
        else:
            super(PickForm, self).__init__(*args, **kwargs)
    
