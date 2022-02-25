from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from restaurants.models import Restaurant
from .models import Profile
from .forms import UpdateProfileForm


class ProfileView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, slug=slug)
        author = User.objects.get(profile__slug__iexact=slug)
        restaurant_posts = Restaurant.objects.filter(
            author=author,
            approved=True).order_by('-created_on')
        profile_toggle = request.GET.get('posts-favourites-toggle')
        current_list = 'posts'

        if (profile_toggle != '' and profile_toggle is not None and
                profile_toggle != 'Posts'):
            restaurant_posts = Restaurant.objects.filter(
                favourited__username=slug,
                approved=True).order_by('-created_on')
            current_list = 'favourites'

        paginator = Paginator(restaurant_posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Creates copy of GET and removes superfluous additonal 'page' that is
        # added to the url when using pagination and filters.
        # CREDIT = idea came from: (https://stackoverflow.com/questions/
        # 59972694/django-pagination-maintaining-filter-and-order-by)
        get_copy = self.request.GET.copy()
        if get_copy.get('page'):
            get_copy.pop('page')

        return render(
            request,
            'profile.html',
            {
                'profile': profile,
                'current_list': current_list,
                'page_obj': page_obj,
                'get_copy': get_copy,
            }
        )


class EditProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    form_class = UpdateProfileForm

    # Idea for returning only current user related objects came from
    # (https://www.django-antipatterns.com/antipattern/
    # checking-ownership-through-the-userpassestestmixin.html)
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user=self.request.user)

    def form_valid(self, form):
        self.object.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Your profile has been updated.')

        return super().form_valid(form)
