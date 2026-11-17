from django.contrib import admin
from .models import Departments, Users, Employees, EmployeeProfile

# Register your models here.
admin.site.register(Departments)
admin.site.register(Users)
# admin.site.register(Employees)
admin.site.register(EmployeeProfile)

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id","employee_name", "email", "salary", "department", "created_at"]
    search_fields = ["employee_name", "email"]
    list_filter = ["department"]