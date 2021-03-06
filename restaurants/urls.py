from django.urls import path
from . import views

urlpatterns = [
     path('', views.RestaurantList.as_view(), name='restaurants'),
     path('add/', views.AddRestaurant.as_view(),
          name='add_restaurant'),
     path('<slug:slug>/edit/', views.EditRestaurant.as_view(),
          name='edit_restaurant'),
     path('<slug:slug>/delete/', views.DeleteRestaurant.as_view(),
          name='delete_restaurant'),
     path('<slug:slug>/', views.RestaurantDetail.as_view(),
          name='restaurant_detail'),
     path('favourited/<slug:slug>/', views.RestaurantFavourite.as_view(),
          name='restaurant_favourited'),
]
