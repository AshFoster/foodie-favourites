from django.shortcuts import render
from django.views import generic
from django.db.models import Count
from .models import Cuisine, Restaurant, Comment, Dish


class HomeList(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.filter(approved=True).order_by('-created_on')[:2]
    template_name = 'index.html'


class RestaurantList(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.filter(approved=True).order_by('-created_on')
    template_name = 'restaurants.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(RestaurantList, self).get_context_data(**kwargs)

        cuisine_with_restaurant_count = Cuisine.objects.filter(approved=True).annotate(restaurant_count=Count('restaurant_cuisine'))
        cuisine_with_restaurant_count_values = cuisine_with_restaurant_count.values('restaurant_count')
        cuisine_counter = 0
        for cuisine in cuisine_with_restaurant_count_values:
            cuisine_counter += cuisine['restaurant_count']

        context['cuisine_count'] = cuisine_counter
        context['cuisine_list'] = cuisine_with_restaurant_count
        return context
