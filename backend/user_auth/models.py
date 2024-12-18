from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)  
    email = models.EmailField(max_length=255, unique=True)  

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name'] 

    def __str__(self):
        return self.email  
