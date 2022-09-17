from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, PlayerStatusLog

# Create your views here.


def index(response, id):
    p = Player.objects.get(id=id)
    logs = p.playerstatuslog_set.get(id=1)
    return HttpResponse("<h1>Clash of Clans - %s</h1><br></br><p>Exp Level = %s</p>" %(p.name, logs.exp_level))


def profile(response):
    return HttpResponse("Your Profile")
