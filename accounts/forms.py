from allauth.account.forms import SignupForm
from .models import Profile


class CustomSignupForm(SignupForm):

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        Profile.objects.create(
            user=user,
            name='',
        )
        user.save()
        return user
