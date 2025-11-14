from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def place_list(request):

    """If this is a POST request, the user clicked the Add button in the form,. Check if the new
    place is valid, if so, save a new Place to the database, and redirect to this same page. This 
    creates a GET request to this same route.
    
    If not a POST route, or Place is not valid, display a page with a list of places and a form to
    add a new place.
    """

    if request.method == 'POST':
        #create new place
        form = NewPlaceForm(request.POST) # creating from data in the request
        place = form.save(commit=False) # creating a model object from form, does not save changes at this point
        place.user = request.user
        if form.is_valid(): # validation against DB constraint
            place.save()    #saves place to DB
            return redirect('place_list') # reloads homepage

    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name') # information about the user is saved in 'request' and can be accessed from there
    new_place_form = NewPlaceForm( )
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

def about(request):
    author = 'Jacob'
    about = 'A website documenting that Jacob is flying by the seat of his pants trying to figure' \
    'this out, will he? Who knows, will it stick? Maybe. Taking all bets.'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})

@login_required
def palce_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:
            place.visited = True
            place.save()
        else:
            return HttpResponseForbidden()
    return redirect('place_list')

@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    return render(request, 'travel_wishlist/place_detail.html', {'place': place})

@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden