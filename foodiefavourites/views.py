from django.views import generic
from restaurants.models import Restaurant


class HomeRestaurantList(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.filter(
               approved=True).order_by('-created_on')[:2]
    template_name = 'index.html'
