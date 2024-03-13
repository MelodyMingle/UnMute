from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated, SpotifySearch

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('callback', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('search', SpotifySearch.as_view({'get':'list'}), name='spotify_list')
]