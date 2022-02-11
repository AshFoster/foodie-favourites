from django.contrib import admin
from . models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Define list filter for Profile Admin objects."""
    list_filter = ('user', 'name')
