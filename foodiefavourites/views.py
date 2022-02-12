from django.views.generic.base import TemplateView
from restaurants.models import Restaurant


class HomePageView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_restaurants'] = Restaurant.objects.filter(
               approved=True).order_by('-created_on')[:2]
        return context
