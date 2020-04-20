from django.db import models

class Player(models.Model):
	character=models.CharField(max_length=12, default='None')
	
	def __str__(self):
		return self.character

class PlayerSheet(models.Model):
	player=models.ForeignKey(Player, on_delete=models.CASCADE, default='Nobody')
	s1=models.BooleanField(verbose_name="Col. Mustard", default=False)
	s2=models.BooleanField(verbose_name="Prof. Plum", default=False)
	s3=models.BooleanField(verbose_name="Mr. Green", default=False)
	s4=models.BooleanField(verbose_name="Mrs. Peacock", default=False)
	s5=models.BooleanField(verbose_name="Miss Scarlet", default=False)
	s6=models.BooleanField(verbose_name="Mrs. White", default=False)
	w1=models.BooleanField(verbose_name="Knife", default=False)
	w2=models.BooleanField(verbose_name="Candlestick", default=False)
	w3=models.BooleanField(verbose_name="Revolver", default=False)
	w4=models.BooleanField(verbose_name="Rope", default=False)
	w5=models.BooleanField(verbose_name="Lead Pipe", default=False)
	w6=models.BooleanField(verbose_name="Wrench", default=False)
	r1=models.BooleanField(verbose_name="Hall", default=False)
	r2=models.BooleanField(verbose_name="Lounge", default=False)
	r3=models.BooleanField(verbose_name="Dining Room", default=False)
	r4=models.BooleanField(verbose_name="Kitchen", default=False)
	r5=models.BooleanField(verbose_name="Ballroom", default=False)
	r6=models.BooleanField(verbose_name="Conservatory", default=False)
	r7=models.BooleanField(verbose_name="Billiard Room", default=False)
	r8=models.BooleanField(verbose_name="Library", default=False)
	r9=models.BooleanField(verbose_name="Study", default=False)

	def __str__(self):
		return self.player.character
		
class SharedWith(models.Model):
	shared_with=models.BooleanField(default=False)
	player=models.ForeignKey(Player, on_delete=models.CASCADE, default='Nobody')
	card_text=models.CharField(max_length=13, default='Blank')
	
	def __str__(self):
		return self.player.character