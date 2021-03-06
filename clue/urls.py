"""clue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from startpage.views import StartPage, SelectPlayer
from players.views import PlayerPage, ShareCard, AjaxShareCardQuery
from cards.views import ShareSolution

urlpatterns = [
	path('', StartPage.as_view(), name='startpage'),
	path('selectplayer/', SelectPlayer.as_view(), name='selectplayer'),
	path('sharecard/<int:player_pk>/', ShareCard.as_view(), name='sharecard'),
	path('player/<int:pk>/', PlayerPage.as_view(), name='playerpage'),
	path('ajax/share_card_query/', AjaxShareCardQuery, name='ajaxsharecardquery'),
	path('solution/', ShareSolution.as_view(), name='sharesolution'),
    path('admin/', admin.site.urls),
]
