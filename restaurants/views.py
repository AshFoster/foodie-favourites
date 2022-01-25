from django.shortcuts import render
from django.views import generic
from .models import Cuisine, Restaurant, Comment, Dish


class HomeList(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.filter(approved=True).order_by('-created_on')[:2]
    template_name = 'index.html'


class RestaurantList(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.filter(approved=True).order_by('-created_on')
    template_name = 'restaurants.html'
    paginate_by = 6
