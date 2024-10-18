from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.CharField(max_length=1000, blank=True, null=True)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default="None")
    drink = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)

    def __str__(self):
        return self.name