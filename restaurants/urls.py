from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeList.as_view(), name="home"),
    path("restaurants/", views.RestaurantList.as_view(), name="restaurants"),
]
