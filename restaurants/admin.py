from django.contrib import admin
from . models import Cuisine, Restaurant, Comment, Dish


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    """Define actions for Cuisine Admin objects."""
    list_display = ('name', 'approved')
    actions = ['approve_cuisine']

    def approve_cuisine(self, request, queryset):
        """Update approved field to True."""
        queryset.update(approved=True)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Define actions for Restaurant Admin objects."""
    prepopulated_fields = {'slug': ('name',)}
    actions = ['approve_restaurants']

    def approve_restaurants(self, request, queryset):
        """Update approved field to True."""
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Define actions for Comment Admin objects."""
    list_display = ('name', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Update approved field to True."""
        queryset.update(approved=True)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """Define list filter for Dish Admin objects."""
    list_filter = ('name', 'restaurant__name')
