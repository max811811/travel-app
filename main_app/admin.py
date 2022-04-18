from django.contrib import admin

# Register your models here.
from .models import Destination, Attraction, Review

admin.site.register(Destination)
admin.site.register(Attraction)
admin.site.register(Review)