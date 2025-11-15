from django import forms
from .models import Place

# Classes used to create forms based of the model used to create DB

#used when creating a new place
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

#used to allow the select a date from the calendar widget
class DateInput(forms.DateInput):
    input_type = 'date'

#used to create the trip review page when a user has visited a location
class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput()
        }