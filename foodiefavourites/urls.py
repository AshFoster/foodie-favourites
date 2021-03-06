from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path("restaurants/", include("restaurants.urls"), name="restaurant_urls"),
    path("accounts/", include("accounts.urls"), name="account_urls"),
    path("contact/", include("contact.urls"), name="contact_urls"),
]


handler404 = views.handler404
handler500 = views.handler500
