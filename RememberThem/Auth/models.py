from django.db import models

# Create your models here.

class Account(models.Model):
    Email = models.EmailField(max_length=254,unique=True)
    Password = models.CharField(max_length=128)
    FName = models.CharField(max_length=50)
    LName = models.CharField(max_length=50)
    Cellphone = models.CharField(max_length=20)

    IsActive = models.BooleanField(default=True)
    IsStaff = models.BooleanField(default=False)
    IsSuperuser = models.BooleanField(default=False)

    LastLogin = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.FName} {self.LName} - {self.LastLogin}"