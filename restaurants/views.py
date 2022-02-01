from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.db.models import Count
from .models import Cuisine, Restaurant, Comment, Dish


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
        context['range'] = range(5)
        return context


class RestaurantDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Restaurant.objects.filter(approved=True)
        restaurant = get_object_or_404(queryset, slug=slug)
        dishes = restaurant.dishes.order_by('name')
        comments = restaurant.comments.filter(approved=True).order_by('created_on')
        comment_count = restaurant.comments.filter(approved=True).count()
        
        return render(
            request,
            'restaurant_detail.html',
            {
                'restaurant': restaurant,
                'range': range(5),
                'dishes': dishes,
                'comments': comments,
                'comment_count': comment_count,
            },
        )
