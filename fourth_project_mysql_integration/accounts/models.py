from django.db import models

# Create your models here.

class Departments(models.Model):
    department_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.department_name

# accounts_employees
class Employees(models.Model):
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "employees"
        ordering = ["employee_name"]
    
    # def __str__(self):
    #     return self.email


class EmployeeProfile(models.Model):
    employee=models.OneToOneField(Employees, on_delete=models.CASCADE)
    dob = models.DateField()
    profile_picture = models.CharField(max_length=200)
        
# accounts_users
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)