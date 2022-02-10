from django import forms
from crispy_forms.helper import FormHelper
from localflavor.gb.gb_regions import GB_REGION_CHOICES
from . import models

RATING_CHOICES = [tuple([x, x]) for x in range(1, 6)]
GB_REGION_CHOICES = (('', ''),) + GB_REGION_CHOICES


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = models.Restaurant
        fields = ('name', 'description', 'image', 'rating', 'location', 'county', 'cuisine')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['rows'] = 4
        self.fields['rating'].widget = forms.Select(choices=RATING_CHOICES)
        self.fields['county'].widget = forms.Select(choices=GB_REGION_CHOICES)


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = False
        self.fields['content'].widget.attrs['placeholder'] = 'Leave a comment...'
        self.fields['content'].widget.attrs['rows'] = 2
