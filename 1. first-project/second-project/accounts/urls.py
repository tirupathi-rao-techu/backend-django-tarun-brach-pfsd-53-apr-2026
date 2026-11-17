from django.urls import path
from .views import home, tarun, rehman

urlpatterns = [
    path("", home),
    path("tarun/", tarun),
    path("rehman/", rehman)
]