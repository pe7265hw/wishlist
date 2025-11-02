from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name="place_list"),
    path('about', views.about, name='about'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited', views.palce_was_visited, name='place_was_visited')
]