from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

# updated Place model which includes infomration on which user is uploading informaiton
# the name of location, whether it was visited, notes, date visited and a photo
class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

# overrides save function to check if photo exists and remove old instance, before calling original delete function
    def save(self, *args, **kwargs):
        old_place = Place.objects.filter(pk=self.pk).first()
        if old_place and old_place.photo:
            if old_place.photo != self.photo:
                self.delete_photo(old_place.photo)
        
        super().save(*args, **kwargs)

# deletes photo file location
    def delete_photo(self, photo):
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name) 

# overrides delete photo if no new one is being added then calls original function
    def delete(self, *args, **kwargs):
        if self.photo:
            self.delete_photo(self.photo)

        super().delete(*args, **kwargs)



    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'
        notes_str = self.notes[100:] if self.notes else 'no notes'
        return f'{self.name} visited? {self.visited} on {self.date_visited}. Notes: {notes_str} Photo {photo_str}'