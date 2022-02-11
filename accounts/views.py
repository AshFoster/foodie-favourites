from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Profile


class ProfileView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'profile.html',
            {
                'profile': profile,
            }
        )
