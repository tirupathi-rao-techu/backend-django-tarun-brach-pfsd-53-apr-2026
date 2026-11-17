from django.urls import path, re_path
from .views import dashboard, employees, employeeDetails, profileDetails

# App URLs
urlpatterns = [
    path("", dashboard),
    path("employees/", employees),
    re_path(r"^employees/[0-9]+/$", employeeDetails),
    path("profile/<int:profile_id>/<str:profile_name>/", profileDetails)
]
