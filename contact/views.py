from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import ContactForm


class ContactUs(FormView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        # form.send_email()
        messages.add_message(self.request, messages.SUCCESS, f'Your message has been sent successfully.')
        return super().form_valid(form)
