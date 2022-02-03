from django import forms
from . import models


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = models.Restaurant
        fields = ['name', 'description', 'image', 'rating', 'location', 'cuisine']
