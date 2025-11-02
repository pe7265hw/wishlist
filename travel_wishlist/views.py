from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

def place_list(request):

    if request.method == 'POST':
        #create new place
        form = NewPlaceForm(request.POST) # creating from data in the request
        place = form.save() # creating a model object from form
        if form.is_valid(): # validation against DB constraint
            place.save()    #saves place to DB
            return redirect('place_list') # reloads homepage

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm( )
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

def about(request):
    author = 'Jacob'
    about = 'A website documenting that Jacob is flying by the seat of his pants trying to figure' \
    'this out, will he? Who knows, will it stick? Maybe. Taking all bets.'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})

def palce_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()
    return redirect('place_list')