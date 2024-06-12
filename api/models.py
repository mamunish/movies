from django.db import models
from django.contrib.auth.models import User



# This is the model for the notes
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='watchlist')
    movie_name = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# This is the string representation of the object
    def __str__(self):
        return self.movie_name