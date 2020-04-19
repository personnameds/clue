from django.db import models
from players.models import Player

class Card(models.Model):
	card_text = models.CharField(max_length=13, default='Blank')
	player = models.ForeignKey(Player, on_delete=models.CASCADE, default='Nobody')	
	
	def __str__(self):
		return self.card_text
		
class Solution(models.Model):
	murderer = models.CharField(max_length=13, default='Blank')
	weapon = models.CharField(max_length=13, default='Blank')
	room = models.CharField(max_length=13, default='Blank')
	
	def __str__(self):
		return "%s in the %s with the %s" %(self.murderer,self.room,self.weapon)