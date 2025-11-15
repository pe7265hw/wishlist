from django.urls import path
from . import views

# urls which views.py will need to access
urlpatterns = [
    path('', views.place_list, name="place_list"),
    path('about', views.about, name='about'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited', views.palce_was_visited, name='place_was_visited'),
    path('place/<int:place_pk>', views.place_details, name='place_details'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place')

]