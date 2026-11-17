from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def departments(request):
    return HttpResponse("This is the departments hoem page")

def departmentDetails(request):
    return HttpResponse("This si the depratment detailed page")