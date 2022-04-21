from audioop import reverse
from pyexpat import model
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from .models import Destination, Attraction, Review
from .forms import ReviewForm
from django.views.generic import TemplateView
from .services import get_temptimezone, weather_description

from django.urls import reverse_lazy, reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def destinations_index(request):
	destinations = Destination.objects.all()
	return render(request, 'destinations/index.html', {'destinations': destinations})

def destinations_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    city = Destination.objects.get(id=destination_id)
    temp = get_temptimezone(city)
    temperature_time_zone = {
        "city": city,
        "temp": temp,
    }
    weather = weather_description(city)
    city_weather =  {
        "weather": weather
    }
    # print(weather_description)
    return render(request, 'destinations/detail.html', {'destination': destination, 'temperature_time_zone': temperature_time_zone, 'city_weather': city_weather})
  
def attractions_detail(request, destination_id, attraction_id):
    destination = Destination.objects.get(id=destination_id)
    attraction = Attraction.objects.get(id=attraction_id)
    review_form = ReviewForm()
    return render(request, 'destinations/attractions/detail.html', {'destination': destination, "attraction": attraction, 'review_form': review_form})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def add_review(request, destination_id, attraction_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.attraction_id = attraction_id
        new_review.save()
        print(new_review.rating)
    return redirect('attractions_detail', attraction_id=attraction_id, destination_id=destination_id)

class ReviewUpdate(UpdateView, LoginRequiredMixin):
    model = Review
    fields = ['date', 'rating', 'review_text']

class ReviewDelete(DeleteView, LoginRequiredMixin):
    model = Review
    def get_success_url(self):
        print(self.object.attraction)
        review_id = self.object.attraction.id
        return reverse('attractions_detail', kwargs={'destination_id': self.object.attraction.destination.id, 'attraction_id': self.object.attraction.id})

