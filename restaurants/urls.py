from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='restaurants'),
    path('<slug:slug>/', views.RestaurantDetail.as_view(),
         name='restaurant_detail'),
]
