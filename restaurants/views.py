from django.shortcuts import render
from django.views import generic
from .models import Cuisine, Restaurant, Comment, Dish


class RestaurantList(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
