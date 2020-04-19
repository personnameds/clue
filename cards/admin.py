from django.contrib import admin
from .models import Card, Solution

class CardAdmin(admin.ModelAdmin):
	list_display=('card_text','player')

admin.site.register(Card, CardAdmin)
admin.site.register(Solution)
