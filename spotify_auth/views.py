import os
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()


def get_spotify_oauth():
    """Create and return SpotifyOAuth object"""
    return SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
        scope='user-read-private user-read-email user-top-read user-read-recently-played'
    )


def home(request):
    """Home page with login button"""
    return render(request, 'home.html')


def spotify_login(request):
    """Redirect to Spotify authorization page"""
    sp_oauth = get_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


def spotify_callback(request):
    """Handle the callback from Spotify"""
    sp_oauth = get_spotify_oauth()

    # Get the authorization code from the request
    code = request.GET.get('code')

    if code:
        # Exchange code for access token
        token_info = sp_oauth.get_access_token(code)

        # Store token in session (for now)
        request.session['token_info'] = token_info

        return HttpResponse("Success! You are logged in to Spotify.")
    else:
        error = request.GET.get('error')
        return HttpResponse(f"Error: {error}")