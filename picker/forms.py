from django import forms
from models import Pick, Game

        
class PickForm(forms.ModelForm):
    
    class Meta:
        model = Pick
        fields = ('game', 'winner')
    
    def __init__(self, *args, **kwargs):
        game = kwargs.pop('game', None)
        winner = kwargs.pop('winner', None)
        
        return_value = super(PickForm, self).__init__(*args, **kwargs)
        
        if game:
            self.fields['game'].widget = forms.HiddenInput(attrs={'value': game.id})
        if winner:
            self.fields['winner'].widget = forms.HiddenInput(attrs={'value': winner.id})
        
        return return_value
        
    #     self.fields['winner'].widget = forms.HiddenInput(attrs={'value':team.id})
    #     self.fields['game'].widget = forms.HiddenInput(attrs={'value':game.id})
        
    #     return return_value


