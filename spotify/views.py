from django.shortcuts import render, redirect
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .util import update_or_create_user_tokens, is_spotify_authenticated, get_user_tokens
from .models import SpotifyToken
import requests
from django.http import JsonResponse


class AuthURL(APIView):
    def get(self, request, fornat=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url
        
        return redirect(url)


def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    if error:
        return JsonResponse({'error': 'Authorization failed'}, status=400)

    if code:
        response = post('https://accounts.spotify.com/api/token', data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }).json()
        
        access_token = response.get('access_token')
        token_type = response.get('token_type')
        refresh_token = response.get('refresh_token')
        expires_in = response.get('expires_in')

        # Ensure we have all necessary data before proceeding
        if not access_token or not token_type or not refresh_token or expires_in is None:
            return JsonResponse({'error': 'Invalid token data received from Spotify'}, status=400)

        if not request.session.exists(request.session.session_key):
            request.session.create()

        update_or_create_user_tokens(
            request.session.session_key, access_token, token_type, expires_in, refresh_token)
        
        # Assuming 'home' is a valid named URL in your Django project
        return redirect('home')
    else:
        return JsonResponse({'error': 'Authorization code not provided'}, status=400)


class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(
            self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)
    
class SpotifySearch(GenericViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        # Assuming the session_id can be derived from the request in some manner,
        # for example, from the user's session. Adjust this according to your authentication setup.
        session_id = request.session.session_key

        # Ensure the user is authenticated with Spotify and the token is refreshed if necessary.
        if not is_spotify_authenticated(session_id):
            return Response({'error': 'Authentication with Spotify failed or token expired'}, status=status.HTTP_401_UNAUTHORIZED)

        # Now we can safely assume the token is valid
        token = get_user_tokens(session_id)
        if token is None:
            return Response({'error': 'Spotify token not found'}, status=status.HTTP_404_NOT_FOUND)

        access_token = SpotifyToken.objects.filter(user=session_id)
        headers = {"Authorization": f"Bearer {access_token}"}
        query = request.query_params.get("query")
        type_of_search = "track"
        limit = 20
        offset = 0
        params = {"q": query, "type": type_of_search, "limit": limit, "offset": offset}
        url = "https://api.spotify.com/v1/search"
        response = requests.get(url, headers=headers, params=params)

        return Response(response.json(), status=status.HTTP_200_OK)












