from django import forms
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


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'location', 'favourite_cuisine', 'bio', 'image')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs['rows'] = 4
