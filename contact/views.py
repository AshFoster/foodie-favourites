from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from foodiefavourites.settings import EMAIL_HOST_USER
from .forms import ContactForm


class ContactUs(FormView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        message = self.request.POST.get('message')

        send_mail(
            'From ' + name + ': via Contact Us form - Foodie Favourites',
            message + email,
            EMAIL_HOST_USER,
            [EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your message has been sent successfully.')
        return super().form_valid(form)
