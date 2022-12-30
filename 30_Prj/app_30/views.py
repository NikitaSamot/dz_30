from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h4>About-as</h4>")

def home(request):
    return HttpResponse("<h4>home-as</h4>")

def contacts(request):
    return HttpResponse("<h4>contacts-as</h4>")