import os
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from spotipy.oauth2 import SpotifyOAuth
import spotipy
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

        # Store token in session
        request.session['token_info'] = token_info

        # Create Spotify client with the access token
        sp = spotipy.Spotify(auth=token_info['access_token'])

        # Fetch user profile
        user_profile = sp.current_user()

        # Fetch user's top artists (short term = last 4 weeks)
        top_artists = sp.current_user_top_artists(limit=5, time_range='short_term')

        # Fetch user's top tracks
        top_tracks = sp.current_user_top_tracks(limit=5, time_range='short_term')

        # Store in session for now (later we'll save to database)
        request.session['user_profile'] = user_profile

        # Pass data to template
        context = {
            'user': user_profile,
            'top_artists': top_artists['items'],
            'top_tracks': top_tracks['items']
        }

        return render(request, 'success.html', context)
    else:
        error = request.GET.get('error')
        return HttpResponse(f"Error: {error}")