from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class message(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    approved = models.BooleanField(default=False)
    manager = models.ForeignKey( User, blank=True, null=True,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title