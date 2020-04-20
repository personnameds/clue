from django.contrib import admin
from .models import Player, PlayerSheet, SharedWith

admin.site.register(Player)
admin.site.register(PlayerSheet)
admin.site.register(SharedWith)