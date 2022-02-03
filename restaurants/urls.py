from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='restaurants'),
    path('add-restaurant/', views.AddRestaurant.as_view(),
         name='add_restaurant'),
    path('<slug:slug>/', views.RestaurantDetail.as_view(),
         name='restaurant_detail'),
]
