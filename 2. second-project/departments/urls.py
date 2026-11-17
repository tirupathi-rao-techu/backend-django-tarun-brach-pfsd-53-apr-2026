from django.urls import path, re_path
from .views import departments, departmentDetails

urlpatterns = [
    path("", departments),
    re_path(r"[A-Za-z0-9]+/$",departmentDetails )
]