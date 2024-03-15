from django.db import models
from spottiapp.models import Post  # Import the Post model

# Create your models here.
class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)


class ParsedPlaylist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=255)
    tracks_total = models.IntegerField(default=0)
    url = models.URLField(max_length=200)
    image = models.URLField(max_length=200, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.name