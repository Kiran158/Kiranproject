from django.shortcuts import render
from django.template import loader



def home(request):
    return render(request, "projectapp/home.html")