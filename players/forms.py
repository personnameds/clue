from django import forms
from players.models import PlayerSheet, Player


class PlayerSheetForm(forms.ModelForm):
	class Meta:
		model = PlayerSheet
		fields = ['s1','s2','s3','s4','s5','s6',
				'w1','w2','w3','w4','w5','w6',
				'r1','r2','r3','r4','r5','r6','r7','r8','r9',	
				 ]

#Selection of Player should go in Modal
# 	def __init__(self, *args, **kwargs):
# 		player = kwargs['instance'].player
# 		super(PlayerSheetForm, self).__init__(*args, **kwargs)
# 		self.fields['sharewith'] = forms.ModelChoiceField(queryset=Player.objects.exclude(pk=player.pk),empty_label=None)