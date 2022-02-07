from django import forms
from crispy_forms.helper import FormHelper
from . import models


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = models.Restaurant
        fields = ('name', 'description', 'image', 'rating', 'location', 'cuisine')


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['content'].label = False
        self.fields['content'].widget.attrs['placeholder'] = 'Leave a comment...'
        self.fields['content'].widget.attrs['rows'] = 2
