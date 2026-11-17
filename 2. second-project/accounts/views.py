from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

# Create your views here.
def dashboard(request):
    return HttpResponse("This is the main dashboard page")

def employees(request):
    return HttpResponse("<h1>This si the employees page</h1>")

def employeeDetails(request):
    return HttpResponse("This is the employee detailed page")

def profileDetails(request, profile_id, profile_name):
    print(request.method)
    print(request.path)
    print(request.GET)
    print(request.POST)
    print(request.user)
    print(request.headers)
    
    data = {
        "profile_id":profile_id,
        "profile_nmae":profile_name
    }
    
    print(f"Profile id : {profile_id}")
    print(f"Profile name : {profile_name}")
    # return HttpResponse(f"<h1>This is my profile id is {profile_id} and my name is {profile_name} </h1>")
    # return JsonResponse(data)
    return redirect("/employees/")