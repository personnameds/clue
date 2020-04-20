from django import forms
from players.models import PlayerSheet, Player
from cards.models import Card

class PlayerSheetForm(forms.ModelForm):
	class Meta:
		model = PlayerSheet
		fields = ['s1','s2','s3','s4','s5','s6',
				'w1','w2','w3','w4','w5','w6',
				'r1','r2','r3','r4','r5','r6','r7','r8','r9',	
				 ]

class ShareCardForm(forms.Form):	
	def __init__(self, *args, **kwargs):
		player_pk = kwargs.pop('player_pk')
		player=Player.objects.get(pk=player_pk)
		super(ShareCardForm, self).__init__(*args, **kwargs)
		self.fields['card'] = forms.ModelChoiceField(
						queryset=Card.objects.filter(player=player),
						label='Card',
						empty_label=None,
						widget =forms.RadioSelect,
						)
		self.fields['sharewith'] = forms.ModelChoiceField(queryset=Player.objects.exclude(pk=player_pk),label='Share with',empty_label=None)
