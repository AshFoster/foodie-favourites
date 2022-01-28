from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('restaurants/', views.RestaurantList.as_view(), name='restaurants'),
    path('restaurants/<slug:slug>/', views.RestaurantDetail.as_view(), name='restaurant_detail'),
]
