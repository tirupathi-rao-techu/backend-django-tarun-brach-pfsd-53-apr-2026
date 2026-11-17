from django.urls import path
from .views import homePage,coursesPage

urlpatterns = [
    path("", homePage),
    path("courses/", coursesPage)
]