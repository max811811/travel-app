from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

# Create your models here.
RATING = (
    (0, 'Zero'),
    (1, 'One'),
    (2, 'Two'),
    (3, 'Three'),
    (4, 'Four'),
    (5, 'Five')
)

class Destination(models.Model):
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50, default='')
	country = models.CharField(max_length=30)
	time_zone = models.CharField(max_length=20)
	location_description = models.TextField(max_length=200)
	photo = models.URLField()

	
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.city
		
	def get_absolute_url(self):
		return reverse('', kwargs={'pk': self.id})

class Attraction(models.Model):
	name = models.CharField(max_length=100, default='')
	description = models.CharField(max_length=500)
	location = models.CharField(max_length=100)
	price = models.IntegerField()
	website = models.URLField(default='')
	photo = models.URLField(default='')

	destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('attractions_detail', kwargs={'destination_id': self.destination.id, 'attraction': self.attraction.id, 'pk': self.review.id})
    
class Review(models.Model):
	date = models.DateField('review date')
	rating = models.IntegerField(choices=RATING, default=RATING[0][0])
	review_text = models.TextField(max_length=100)

	attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.get_rating_display()} on {self.date}"
	class Meta:
		ordering = ['date']

	def get_absolute_url(self):
		print(self.attraction.destination)
		return reverse('attractions_detail', kwargs={'destination_id': self.attraction.destination.id, 'attraction_id': self.attraction.id})
