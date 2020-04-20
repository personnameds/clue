from django.shortcuts import render
from cards.models import Solution
from django.views. generic import ListView

class ShareSolution(ListView):
	model = Solution
	template_name='cards/solutionpage.html'
	context_object_name= 'solution'
