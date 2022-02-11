from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeRestaurantList.as_view(), name='home'),
    path("restaurants/", include("restaurants.urls"), name="restaurant_urls"),
    path("accounts/", include("accounts.urls"), name="account_urls"),
]
