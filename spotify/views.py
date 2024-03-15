from django.shortcuts import render, redirect
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .util import update_or_create_user_tokens, is_spotify_authenticated, get_user_tokens, refresh_spotify_token
from .models import SpotifyToken, ParsedPlaylist
import requests


class AuthURL(APIView):
    def get(self, request, fornat=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-read-private'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return redirect(url)


def spotify_callback(request, format=None):
    print('SPOTIFY CALLBACK WORKS!!!!')
    code = request.GET.get('code')
    print('I GOT THE DMAN CODE', code)
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()
    print('spotify callback!!', response)

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')
    
    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(
        request.session.session_key, access_token, token_type, expires_in, refresh_token)

    return redirect('/')


class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(
            self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)
    
class SpotifySearch(GenericViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        
        session_id = self.request.session.session_key
        print('session id', request.session)

        if not is_spotify_authenticated(session_id) and not refresh_spotify_token(session_id):
            return Response({'error': 'Failed to authenticate with Spotify'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token = get_user_tokens(session_id)
        if token is None:
            return Response({'error': 'No Spotify token found'}, status=status.HTTP_404_NOT_FOUND)

        access_token = token.access_token
        headers = {"Authorization": f"Bearer {access_token}"}
        query = request.query_params.get("query")
        type_of_search = "track"
        limit = 20
        offset = 0
        params = {"q": query, "type": type_of_search, "limit": limit, "offset": offset}
        url = "https://api.spotify.com/v1/search"
        response = requests.get(url, headers=headers, params=params)

        return Response(response.json(), status=status.HTTP_200_OK)

class SpotifySearchPlaylist(GenericViewSet):
    permission_classes = (AllowAny,)
    
    def list(self, request):
        
        # session_id = self.request.session.session_key
    
        # if not is_spotify_authenticated(session_id) and not refresh_spotify_token(session_id):
        #     return Response({'error': 'Failed to authenticate with Spotify'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # token = get_user_tokens(session_id)
        # if token is None:
        #     return Response({'error': 'No Spotify token found'}, status=status.HTTP_404_NOT_FOUND)

        # access_token = token.access_token
        # headers = {"Authorization": f"Bearer {access_token}"}
        # query = {}
        # limit = 20
        # offset = 0
        # params = {'q': query,}
        # url = "https://api.spotify.com/v1/me/playlists"
        

        response = {
            "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20",
            "limit": 20,
            "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
            "offset": 0,
            "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
            "total": 4,
            "items": [
                {
                "collaborative": "false",
                "description": "string",
                "external_urls": {
                    "spotify": "string"
                },
                "href": "string",
                "id": "string",
                "images": [
                    {
                    "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228",
                    "height": 300,
                    "width": 300
                    }
                ],
                "name": "string",
                "owner": {
                    "external_urls": {
                    "spotify": "string"
                    },
                    "followers": {
                    "href": "string",
                    "total": 0
                    },
                    "href": "string",
                    "id": "string",
                    "type": "user",
                    "uri": "string",
                    "display_name": "string"
                },
                "public": "false",
                "snapshot_id": "string",
                "tracks": {
                    "href": "string",
                    "total": 0
                },
                "type": "string",
                "uri": "string"
            }
        ]
        }    


        data = response
        playlists = data['items']
        parsed_playlists = []
        for playlist in playlists:
            parsed_playlist = {
                "name": playlist['name'],
                "description": playlist['description'],
                "owner": playlist['owner']['display_name'],
                "tracks_total": playlist['tracks']['total'],
                "url": playlist['external_urls']['spotify'],
                "image": playlist['images'][0]['url'] if playlist['images'] else None
            }
            print("go")
            # Create an instance of ParsedPlaylist and save it
            parsed_playlist_instance = ParsedPlaylist.objects.create(
                name=parsed_playlist['name'],
                description=parsed_playlist['description'],
                owner=parsed_playlist['owner'],
                tracks_total=parsed_playlist['tracks_total'],
                url=parsed_playlist['url'],
                image=parsed_playlist['image']
            )
            parsed_playlists.append(parsed_playlist_instance)
            
        # return Response(parsed_playlists, status=status.HTTP_200_OK)
        playlists = ParsedPlaylist.objects.all()  # Retrieve all ParsedPlaylist instances
        return render(request, 'home.html', {'playlists': playlists})

