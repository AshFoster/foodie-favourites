from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count
from .models import Cuisine, Restaurant, Comment, Dish
from .forms import AddRestaurantForm, CommentForm


class RestaurantList(generic.ListView):
    """
    Restaurant List class based view to show Restaurant model on
    restaurants.html
    """
    model = Restaurant
    queryset = Restaurant.objects.filter(approved=True).order_by('-created_on')
    template_name = 'restaurants.html'
    paginate_by = 3

    def get_queryset(self):
        cuisine_filter = self.request.GET.get('cuisine-filter')
        location_filter = self.request.GET.get('location-filter')

        if cuisine_filter != '' and cuisine_filter is not None and cuisine_filter != 'All':
            self.queryset = self.queryset.filter(cuisine__name=cuisine_filter)

        if location_filter != '' and location_filter is not None and location_filter != 'All':
            self.queryset = self.queryset.filter(county__icontains=location_filter)

        return self.queryset

    def get_context_data(self, **kwargs):
        """
        The get_context_data function sets the relevant context data
        to be used in restaurants.html
        """
        context = super(RestaurantList, self).get_context_data(**kwargs)
        
        restaurants = Restaurant.objects.filter(approved=True)
        location_filter = self.request.GET.get('location-filter')
        cuisine_string = ''

        if location_filter == 'All':
            for restaurant in restaurants:
                cuisine_string += restaurant.list_cuisines() + ', '
        else:
            for restaurant in restaurants:
                if restaurant.county == location_filter:
                    cuisine_string += restaurant.list_cuisines() + ', '

        cuisine_string = cuisine_string[:len(cuisine_string)-2]
        cuisine_list = cuisine_string.split(', ')
        restaurant_cuisines = {}
        restaurant_cuisines_count = 0

        for cuisine in cuisine_list:
            restaurant_cuisines_count += 1
            if cuisine not in restaurant_cuisines:
                restaurant_cuisines[cuisine] = 1
            else:
                restaurant_cuisines[cuisine] = restaurant_cuisines[cuisine] + 1

        cuisine_filter = self.request.GET.get('cuisine-filter')
        restaurant_locations = {}
        restaurant_locations_count = 0

        if cuisine_filter == 'All':
            for restaurant in restaurants:
                restaurant_locations_count += 1
                if restaurant.county not in restaurant_locations:
                    restaurant_locations[restaurant.county] = 1
                else:
                    restaurant_locations[restaurant.county] = restaurant_locations[restaurant.county] + 1
        else:
            for restaurant in restaurants:
                print(restaurant.list_cuisines())
                if cuisine_filter in restaurant.list_cuisines():
                    print(restaurant.list_cuisines())
                    restaurant_locations_count += 1
                    if restaurant.county not in restaurant_locations:
                        restaurant_locations[restaurant.county] = 1
                    else:
                        restaurant_locations[restaurant.county] = restaurant_locations[restaurant.county] + 1
        
        get_copy = self.request.GET.copy()
        if get_copy.get('page'):
            get_copy.pop('page')

        context['cuisine_count'] = restaurant_cuisines_count
        context['cuisine_list'] = restaurant_cuisines
        context['location_count'] = restaurant_locations_count
        context['location_list'] = restaurant_locations
        context['range'] = range(5)
        context['get_copy'] = get_copy
        return context


class RestaurantDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Restaurant.objects.filter(approved=True)
        restaurant = get_object_or_404(queryset, slug=slug)
        dishes = restaurant.dishes.order_by('name')
        comments = restaurant.comments.filter(approved=True).order_by('created_on')
        comment_count = restaurant.comments.filter(approved=True).count()
        liked = False
        if restaurant.favourited.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'restaurant_detail.html',
            {
                'restaurant': restaurant,
                'range': range(5),
                'dishes': dishes,
                'comments': comments,
                'commented': False,
                'comment_count': comment_count,
                'comment_form': CommentForm(),
                'liked': liked,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Restaurant.objects.filter(approved=True)
        restaurant = get_object_or_404(queryset, slug=slug)
        dishes = restaurant.dishes.order_by('name')
        comments = restaurant.comments.filter(approved=True).order_by('created_on')
        comment_count = restaurant.comments.filter(approved=True).count()
        liked = False
        if restaurant.favourited.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.restaurant = restaurant
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'restaurant_detail.html',
            {
                'restaurant': restaurant,
                'range': range(5),
                'dishes': dishes,
                'comments': comments,
                'commented': True,
                'comment_count': comment_count,
                'comment_form': CommentForm(),
                'liked': liked,
            },
        )


class AddRestaurant(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = 'add_restaurant.html'
    form_class = AddRestaurantForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        form.save_m2m()

        dishes = self.request.POST['dishes-string'].split(',')
        for dish in dishes:
            Dish.objects.create(
                restaurant=Restaurant.objects.get(id=self.object.id),
                name=dish
            ).save()

        # messages.add_message(self.request, messages.SUCCESS, f'{self.object.name} has been sent for approval.')
        messages.add_message(self.request, messages.SUCCESS, f'"{self.object.name}" has been added.')

        return super().form_valid(form)


class EditRestaurant(LoginRequiredMixin, UpdateView):
    model = Restaurant
    template_name = 'add_restaurant.html'
    form_class = AddRestaurantForm

    def get_context_data(self, **kwargs):
        context = super(EditRestaurant, self).get_context_data(**kwargs)
        dishes = self.object.dishes.order_by('name')
        context['dishes'] = dishes

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        form.save_m2m()

        original_dishes = Dish.objects.filter(restaurant=self.object.id)
        for dish in original_dishes:
            dish.delete()

        dishes = self.request.POST['dishes-string'].split(',')
        for dish in dishes:
            Dish.objects.create(
                restaurant=Restaurant.objects.get(id=self.object.id),
                name=dish
            ).save()

        # messages.add_message(self.request, messages.SUCCESS, f'{self.object.name} has been sent for approval.')
        messages.add_message(self.request, messages.SUCCESS, f'"{self.object.name}" has been updated.')

        return super().form_valid(form)


class DeleteRestaurant(LoginRequiredMixin, DeleteView):
    model = Restaurant
    template_name = 'restaurant_confirm_delete.html'
    success_url = reverse_lazy('restaurants')
    
    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Restaurant has been deleted.')
        return super(DeleteRestaurant, self).delete(request, *args, **kwargs)


class RestaurantLike(View):

    def post(self, request, slug, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, slug=slug)
        if restaurant.favourited.filter(id=request.user.id).exists():
            restaurant.favourited.remove(request.user)
        else:
            restaurant.favourited.add(request.user)

        return HttpResponseRedirect(reverse('restaurant_detail', args=[slug]))
