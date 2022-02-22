from django.views.generic.base import TemplateView
from django.shortcuts import render
from restaurants.models import Restaurant


class HomePageView(TemplateView):
    """
    Class based view for index.html.
    Queries the two most recent restaurant posts.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        Returns 'latest_restaurants' context to be used with index.html.
        """
        context = super().get_context_data(**kwargs)
        context['latest_restaurants'] = Restaurant.objects.filter(
               approved=True).order_by('-created_on')[:2]
        return context


def handler404(request, exception):
    """
    404 error handler view
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    500 error handler view
    """
    return render(request, '500.html', status=500)
