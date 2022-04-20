import os 
import requests

def get_temptimezone(city):
        geocoding = requests.post(f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key=AIzaSyC6L-lKIsvE0uRCMwLJKrITheGumyORIME")
        transgeocodes = geocoding.json()
        lat = transgeocodes["results"][0]["geometry"]["location"]["lat"]
        lon = transgeocodes["results"][0]["geometry"]["location"]["lng"]
        allWeatherDataJson = requests.post(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b70e5243385456b84556f52c7008f578")
        allWeatherData = allWeatherDataJson.json()
        temperatureKelvins = allWeatherData["main"]["temp"]
        temperatureF = int((temperatureKelvins-273.15)*9/5+32) 
        timezone = allWeatherData["timezone"]
        
        return temperatureF