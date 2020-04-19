from django import forms


class SetupForm(forms.Form):
    PLAYERS = (
        ("CM", "Col. Mustard"),
        ("PP", "Prof. Plum"),
        ("MG", "Mr. Green"),
        ("MP", "Mrs. Peacock"),
        ("MS", "Miss Scarlet"),
        ("MW", "Mrs. White"),
    )
    players = forms.MultipleChoiceField(label='Whose Playing?',widget=forms.CheckboxSelectMultiple, choices=PLAYERS)
    
    def clean_players(self):
    	data = self.cleaned_data['players']
    	count=len(data)
    	if count < 3:
    		raise forms.ValidationError("You need a minimum of 3 players.")
    	return data