from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

ROLE_CHOICES = [
    ('super_admin', "Super Admin"),
    ('admin', "Admin"),
    ('manager', "Manager"), 
    ('employee', "Employee"),
    ('user', "User"),
]


class User(AbstractUser):
    mobile_number = models.BigIntegerField(max_length=15, null=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="user")
    otp = models.CharField(max_length=6, null=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        db_table = "User"
    
    def __str__(self):
        return self.username