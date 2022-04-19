from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations_index, name='index'),
    path('destinations/<int:destination_id>/', views.destinations_detail, name='detail'),
    path('destinations/<int:destination_id>/attractions/<int:attraction_id>/', views.attractions_detail, name="attractions_detail"),
    path('attractions/<int:attraction_id>/', views.add_review, name='add_review'),
]