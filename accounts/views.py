from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from .models import Profile
from restaurants.models import Restaurant


class ProfileView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, slug=slug)
        author = User.objects.get(username=slug)
        restaurant_posts = Restaurant.objects.filter(author=author, approved=True).order_by('-created_on')
        profile_toggle = request.GET.get('posts-favourites-toggle')
        current_list = 'posts'

        if profile_toggle != '' and profile_toggle is not None and profile_toggle != 'Posts':
            restaurant_posts = Restaurant.objects.filter(favourited__username=slug, approved=True).order_by('-created_on')
            current_list = 'favourites'

        return render(
            request,
            'profile.html',
            {
                'profile': profile,
                'restaurant_posts': restaurant_posts,
                'current_list': current_list,
            }
        )
