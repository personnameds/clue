from django.shortcuts import render
from django.views.generic.edit import UpdateView, FormView
from django.views. generic import ListView
from players.forms import PlayerSheetForm, ShareCardForm
from cards.models import Card
from players.models import PlayerSheet, Player, SharedWith
from django.urls import reverse
from django.http import JsonResponse

def AjaxShareCardQuery(request):
	player_name = request.GET.get('player',None)
	player=Player.objects.get(character=player_name)
	sharedwith=SharedWith.objects.get(player=player)
	if sharedwith.shared_with:
		card_text=sharedwith.card_text
		data = {'response':True,
				'card_text':card_text,
				}
		sharedwith.shared_with=False
		sharedwith.card_text='None'
		sharedwith.save()
	else:
		data = {'response':False}
	return JsonResponse(data)

class PlayerPage(UpdateView):
	model = PlayerSheet
	form_class = PlayerSheetForm
	template_name='players/playerpage.html'
	context_object_name= 'player'

	def get_success_url(self, **kwargs):
		player_pk=self.object.player.pk
		return reverse('sharecard', kwargs={'player_pk':player_pk})

class ShareCard(FormView):
	form_class= ShareCardForm
	template_name= "players/sharecard.html"
	context_object_name = 'card_list'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		player=Player.objects.get(pk=self.kwargs['player_pk'])
		context['player'] = player
		return context
	
	def get_form_kwargs(self):
		kwargs = super( ShareCard, self).get_form_kwargs()
		# update the kwargs for the form init method with yours
		kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
		return kwargs

	def form_valid(self, form):
		self.sharewith=form.cleaned_data['sharewith']
		self.card=form.cleaned_data['card']
		self.player_pk=self.kwargs['player_pk']
		sharedwith=SharedWith.objects.get(player=self.sharewith)
		sharedwith.shared_with=True
		sharedwith.card_text=self.card.card_text
		sharedwith.save()
		return super().form_valid(form)
	
	def get_success_url(self, **kwargs):
		player_sheet=PlayerSheet.objects.get(player__pk=self.player_pk)
		return reverse('playerpage', kwargs={'pk':player_sheet.pk})