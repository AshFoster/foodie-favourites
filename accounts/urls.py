from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/<slug:slug>/', views.ProfileView.as_view(),
         name='profile'),
]
