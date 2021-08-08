from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, "Portfolio/home.html", {'projects': projects})

