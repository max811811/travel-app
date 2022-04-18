from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    time_zone = models.CharField(max_length=20)
    location_description = models.TextField(max_length=200)
  # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('')