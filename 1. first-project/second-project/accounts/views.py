from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse("This is my first page of django application")

def tarun(request):
    return HttpResponse("This si the Tarun Portfolio")

def rehman(request):
    return HttpResponse("<h1>This is the rehman portfolio</h1><p>THis si the paragraph tag</p><a href='https://youtube.com' target='_blank'>Go to Google</a>")