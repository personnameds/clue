from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from startpage.forms import SetupForm
from random import shuffle
from cards.models import Solution, Card
from players.models import Player, PlayerSheet, SharedWith
from itertools import cycle
from django.urls import reverse_lazy
import random

PLAYER_DICT = {
	"CM": "Col. Mustard",
	"PP": "Prof. Plum",
	"MG": "Mr. Green",
	"MP": "Mrs. Peacock",
	"MS": "Miss Scarlet",
	"MW": "Mrs. White",
	}

SUSPECTS=("Col. Mustard","Prof. Plum","Mr. Green","Mrs. Peacock","Miss Scarlet","Mrs. White")
WEAPONS=("Knife","Candlestick","Revolver","Rope","Lead Pipe","Wrench")
ROOMS=("Hall","Lounge","Dining Room","Kitchen","Ballroom","Conservatory","Billiard Room","Library","Study")

def DealCards():

	players=Player.objects.all()
	num_players=len(players)
	
	#Create Card List
	card_list=[0]*18
	i=0
	while i < 22:
		for j in range(num_players):	
			if i+j < 18:
				card_list[i+j]=j+1
		i=i+num_players

	shuffle(card_list)
	
	#Clear solution
	Solution.objects.all().delete()
	
	s=random.randint(0,5)
	suspect=SUSPECTS[s]
	w=random.randint(0,5)
	weapon=WEAPONS[w]
	r=random.randint(0,8)
	room=ROOMS[r]


	solution=Solution(
		murderer=suspect,
		weapon=weapon,
		room=room,
		)
	solution.save()

	#Add Solution Cards to Card List
	card_list.insert(s,0)
	card_list.insert(w+6,0)
	card_list.insert(r+12,0)
	
	#Create cards
	Card.objects.all().delete()
	all_cards=SUSPECTS+WEAPONS+ROOMS
	for n, player_num in enumerate(card_list):
		if player_num != 0:
			card=Card(
				player=players[player_num-1],
				card_text=all_cards[n],
			)
			card.save()
			
	#Initialize Player Sheets
	p=0
	all_sheets=[]
	for player in players:
		player_list=[False]*21
		p=p+1
		for n, card in enumerate(card_list):
			if card == p:
				player_list[n] = True
		
		player_list.insert(0,player)
		all_sheets.append(player_list)

	PlayerSheet.objects.all().delete()

	for player_sheet in all_sheets:
		p=PlayerSheet(
			player=player_sheet[0],
			s1=player_sheet[1],
			s2=player_sheet[2],
			s3=player_sheet[3],
			s4=player_sheet[4],
			s5=player_sheet[5],
			s6=player_sheet[6],
			w1=player_sheet[7],
			w2=player_sheet[8],
			w3=player_sheet[9],
			w4=player_sheet[10],
			w5=player_sheet[11],
			w6=player_sheet[12],
			r1=player_sheet[13],
			r2=player_sheet[14],
			r3=player_sheet[15],
			r4=player_sheet[16],
			r5=player_sheet[17],
			r6=player_sheet[18],
			r7=player_sheet[19],
			r8=player_sheet[20],
			r9=player_sheet[21],
			)
		p.save()

class StartPage(FormView):
	template_name="startpage/startpage.html"
	form_class = SetupForm
	success_url = reverse_lazy('selectplayer')

	def form_valid(self, form):
		
		Player.objects.all().delete()
		players=form.cleaned_data['players']
		for player in players:
			player=Player(
				character=PLAYER_DICT[player],
				)
			player.save()
			
			sharedwith=SharedWith(
				shared_with=False,
				player=player,
				card_text='None',
				)
			sharedwith.save()
		
		DealCards()
		return super().form_valid(form)

class SelectPlayer(ListView):
	model = PlayerSheet
	template_name= "startpage/selectplayer.html"
	context_object_name = 'playersheet_list'