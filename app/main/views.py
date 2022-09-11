from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("Clash of Clans")


def profile(response):
    return HttpResponse("Your Profile")
