from django import forms
from allauth.account.forms import SignupForm
from .models import Profile


class CustomSignupForm(SignupForm):
    """
    Custom form class inheriting from SignUpForm.
    Used to create new Profile object linked to User
    when a new accounts are registered.
    """
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        Profile.objects.create(
            user=user)
        user.save()
        return user


class UpdateProfileForm(forms.ModelForm):
    """
    Custom form used for editing users' profiles
    """
    class Meta:
        model = Profile
        fields = ('name', 'location', 'favourite_cuisine', 'bio', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs['rows'] = 4
