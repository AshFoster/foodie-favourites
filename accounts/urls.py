from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/<slug:slug>/', views.ProfileView.as_view(),
         name='profile'),
    path('profile/<slug:slug>/edit/', views.EditProfile.as_view(),
         name='edit_profile'),
]
