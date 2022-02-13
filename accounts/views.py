from django.shortcuts import render, get_object_or_404
from django.views import  generic, View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from restaurants.models import Restaurant
from .models import Profile


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
        
        paginator = Paginator(restaurant_posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

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
