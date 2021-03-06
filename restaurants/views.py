from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from foodiefavourites.settings import EMAIL_HOST_USER
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
    restaurant_cuisines = {}
    restaurant_cuisines_count = 0
    restaurant_locations = {}
    restaurant_locations_count = 0

    def get_queryset(self):
        cuisine_filter = self.request.GET.get('cuisine-filter')
        location_filter = self.request.GET.get('location-filter')
        search_restaurants = self.request.GET.get('search-restaurants')

        if (cuisine_filter != '' and cuisine_filter is not None and
                cuisine_filter != 'All'):
            self.queryset = self.queryset.filter(cuisine__name=cuisine_filter)

        if (location_filter != '' and location_filter is not None and
                location_filter != 'All'):
            self.queryset = self.queryset.filter(
                county__icontains=location_filter)

        if search_restaurants != '' and search_restaurants is not None:
            self.queryset = self.queryset.filter(
                name__icontains=search_restaurants)

        return self.queryset

    def set_cuisine_and_location_context(self, restaurants):
        """
        Sets cuisine and location related variables to be used as context
        for the filters section of restaurants.html
        """
        location_filter = self.request.GET.get('location-filter')
        cuisine_string = ''

        if (location_filter == 'All' or location_filter == '' or
                location_filter is None):
            for restaurant in restaurants:
                cuisine_string += restaurant.list_cuisines() + ', '
        else:
            for restaurant in restaurants:
                if restaurant.county == location_filter:
                    cuisine_string += restaurant.list_cuisines() + ', '

        if cuisine_string != '':
            cuisine_string = cuisine_string[:len(cuisine_string)-2]
            cuisine_list = cuisine_string.split(', ')
        else:
            cuisine_list = []

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

        if (cuisine_filter == 'All' or cuisine_filter == '' or
                cuisine_filter is None):
            for restaurant in restaurants:
                restaurant_locations_count += 1
                if restaurant.county not in restaurant_locations:
                    restaurant_locations[restaurant.county] = 1
                else:
                    restaurant_locations[
                        restaurant.county] = restaurant_locations[
                            restaurant.county] + 1
        else:
            for restaurant in restaurants:
                if cuisine_filter in restaurant.list_cuisines():
                    restaurant_locations_count += 1
                    if restaurant.county not in restaurant_locations:
                        restaurant_locations[restaurant.county] = 1
                    else:
                        restaurant_locations[
                            restaurant.county] = restaurant_locations[
                                restaurant.county] + 1

        self.restaurant_cuisines = restaurant_cuisines
        self.restaurant_cuisines_count = restaurant_cuisines_count
        self.restaurant_locations = restaurant_locations
        self.restaurant_locations_count = restaurant_locations_count

    def get_context_data(self, **kwargs):
        """
        Sets context data to be used in restaurants.html
        """
        context = super(RestaurantList, self).get_context_data(**kwargs)

        restaurants = Restaurant.objects.filter(approved=True)
        search_restaurants = self.request.GET.get('search-restaurants')

        if search_restaurants != '' and search_restaurants is not None:
            restaurants = restaurants.filter(
                name__icontains=search_restaurants)

        self.set_cuisine_and_location_context(restaurants)

        # Creates copy of GET and removes superfluous additonal 'page' that is
        # added to the url when using pagination and filters.
        # CREDIT = idea came from: (https://stackoverflow.com/questions/
        # 59972694/django-pagination-maintaining-filter-and-order-by)
        get_copy = self.request.GET.copy()
        if get_copy.get('page'):
            get_copy.pop('page')

        context['cuisine_count'] = self.restaurant_cuisines_count
        context['cuisine_list'] = self.restaurant_cuisines
        context['location_count'] = self.restaurant_locations_count
        context['location_list'] = self.restaurant_locations
        context['range'] = range(5)
        context['get_copy'] = get_copy
        return context


class RestaurantDetail(View):
    """
    Restaurant Detail class based view to show individual Restaurant model
    objects on restaurant_detail.html
    """
    def get(self, request, slug, *args, **kwargs):
        # CREDIT - idea for get method structure came from
        # Code Institute's blog walkthrough project
        queryset = Restaurant.objects.filter(approved=True)
        restaurant = get_object_or_404(queryset, slug=slug)
        dishes = restaurant.dishes.order_by('name')
        comments = restaurant.comments.filter(
            approved=True).order_by('created_on')
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
        # CREDIT - idea for post method structure came from
        # Code Institute's blog walkthrough project
        queryset = Restaurant.objects.filter(approved=True)
        restaurant = get_object_or_404(queryset, slug=slug)
        dishes = restaurant.dishes.order_by('name')
        comments = restaurant.comments.filter(
            approved=True).order_by('created_on')
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
            email_subject = ('Comment from: ' + comment_form.instance.name +
                             ' - Foodie Favourites')
            email_message = ('A comment on "' + str(restaurant) +
                             ' "has been submitted and needs approval.')

            send_mail(
                email_subject,
                email_message,
                EMAIL_HOST_USER,
                [EMAIL_HOST_USER],
                fail_silently=False,
            )
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
    """
    Class based view used for adding restaurant objects via the
    add restaurant form on add_restaurant.html
    """
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

        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'"{self.object.name}" has been added.')

        return super().form_valid(form)


class EditRestaurant(LoginRequiredMixin, UpdateView):
    """
    Class based view used for editing restaurant objects via the
    add restaurant form on add_restaurant.html
    """
    model = Restaurant
    template_name = 'add_restaurant.html'
    form_class = AddRestaurantForm

    # Idea for returning only current user related objects came from
    # (https://www.django-antipatterns.com/antipattern/
    # checking-ownership-through-the-userpassestestmixin.html)
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user
        )

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

        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'"{self.object.name}" has been updated.')

        return super().form_valid(form)


class DeleteRestaurant(LoginRequiredMixin, DeleteView):
    """
    Class based view used for deleting restaurant objects
    """
    model = Restaurant
    template_name = 'restaurant_confirm_delete.html'
    success_url = reverse_lazy('restaurants')

    # Idea for returning only current user related objects came from
    # (https://www.django-antipatterns.com/antipattern/
    # checking-ownership-through-the-userpassestestmixin.html)
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            author=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Restaurant has been deleted.')
        return super(DeleteRestaurant, self).delete(request, *args, **kwargs)


class RestaurantFavourite(View):
    """
    Class based view used for favouriting restaurant objects
    """
    # CREDIT - idea for restaurant favourite post method structure came from
    # Code Institute's blog walkthrough project
    def post(self, request, slug, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, slug=slug)
        if restaurant.favourited.filter(id=request.user.id).exists():
            restaurant.favourited.remove(request.user)
        else:
            restaurant.favourited.add(request.user)

        return HttpResponseRedirect(reverse('restaurant_detail', args=[slug]))
