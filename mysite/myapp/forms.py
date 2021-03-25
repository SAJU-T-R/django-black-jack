from django import forms
from myapp.models import GameCard, GameBet

class FormName(forms.ModelForm):
    class Meta():
        model= GameBet
        fields = '__all__'

class FormHit(forms.ModelForm):
    class Meta():
        model= GameCard
        fields ='__all__'
