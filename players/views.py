from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views. generic import ListView
from players.forms import PlayerSheetForm
from cards.models import Card
from players.models import PlayerSheet, Player
from django.urls import reverse

class PlayerPage(UpdateView):
	model = PlayerSheet
	form_class = PlayerSheetForm
	template_name='players/playerpage.html'
	context_object_name= 'player'
	
	def form_valid(self, form):
		self.form = form
		return super().form_valid(form)
		
	def get_success_url(self, **kwargs):
		player_pk=self.object.player.pk
		return reverse('sharecard', kwargs={'player_pk':player_pk})


class ShareCard(ListView):
	model = Card
	template_name= "players/sharecard.html"
	context_object_name = 'card_list'
	
	def get_queryset(self):
		player=Player.objects.get(pk=self.kwargs['player_pk'])
		return Card.objects.filter(player=player)
	
# Selection of Player should go in Modal
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		sharewith=Player.objects.get(pk=self.kwargs['sharewith_pk'])
# 		context['sharewith'] = sharewith
# 		return context