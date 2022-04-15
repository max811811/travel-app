from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
  # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('')