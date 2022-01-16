from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class BaseTimeStampModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True
        


