from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

ROLE_CHOICES = [
    ('super_admin', "Super Admin"),
    ('admin', "Admin"),
    ('manager', "Manager"), 
    ('employee', "Employee"),
    ('user', "User"),
]

class UserManager(BaseUserManager):
    def create_user(self, username, email, mobile_number, password=None, role="user"):
        
        if not email:
            return ValueError("Email is required")
        
        email = self.normalize_email(email) # ADMIN@GMAIL.COM admin@gmail.com
        user = self.model(email=email, username=username, mobile_number=mobile_number, role=role)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username, email, mobile_number, password):
        user = self.create_user(
            username=username, email=email, mobile_number=mobile_number, password=password, role="super_admin"
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=100, unique=True)
    mobile_number = models.BigIntegerField(max_length=15, null=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default="user")
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "mobile_number"]
    
    class Meta:
        db_table = "User"
    
    def __str__(self):
        return self.username