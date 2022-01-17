from . import views
from django.urls import path

urlpatterns = [
    path("", views.RestaurantList.as_view(), name="home"),
]
