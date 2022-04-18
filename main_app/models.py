from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Destination(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    time_zone = models.CharField(max_length=20)
    location_description = models.TextField(max_length=200)
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return reverse('')

class Attraction(models.Model):
	description = models.CharField(max_length=500)
	location = models.CharField(max_length=100)
	price = models.IntegerField()

	destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
