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


import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv
from collections import Counter

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
    code = request.GET.get('code')

    if code:
        token_info = sp_oauth.get_access_token(code)
        request.session['token_info'] = token_info

        sp = spotipy.Spotify(auth=token_info['access_token'])
        user_profile = sp.current_user()

        # Gather data from different time periods
        top_artists_short = sp.current_user_top_artists(limit=20, time_range='short_term')
        top_artists_long = sp.current_user_top_artists(limit=20, time_range='long_term')
        top_tracks = sp.current_user_top_tracks(limit=50, time_range='short_term')

        # Extract genres from artists
        all_genres = []
        for artist in top_artists_short['items']:
            all_genres.extend(artist.get('genres', []))

        # Analyze music taste
        genre_counter = Counter(all_genres)
        top_genres = genre_counter.most_common(10)

        # Calculate music personality metrics
        metrics = {
            'genre_diversity': len(set(all_genres)),
            'mainstream_score': sum(a['popularity'] for a in top_artists_short['items']) / len(
                top_artists_short['items']) if top_artists_short['items'] else 50,
            'loyalty_score': len(set(a['id'] for a in top_artists_long['items']) & set(
                a['id'] for a in top_artists_short['items'])) / len(top_artists_short['items']) if top_artists_short[
                'items'] else 0.5,
            'explicit_preference': sum(1 for t in top_tracks['items'] if t.get('explicit', False)) / len(
                top_tracks['items']) if top_tracks['items'] else 0,
            'avg_track_popularity': sum(t['popularity'] for t in top_tracks['items']) / len(top_tracks['items']) if
            top_tracks['items'] else 50,
        }

        # Map genres to moods/characteristics
        genre_moods = analyze_genre_mood(top_genres)

        # Generate Notion face parameters
        face_params, face_explanation = generate_face_from_taste(metrics, genre_moods, top_genres)

        context = {
            'user': user_profile,
            'top_artists': top_artists_short['items'][:5],
            'top_genres': top_genres[:5],
            'metrics': metrics,
            'genre_moods': genre_moods,
            'face_url': f"https://faces.notion.com/?face={face_params}",
            'face_params': face_params,
            'face_explanation': face_explanation,
        }

        return render(request, 'face_result.html', context)
    else:
        error = request.GET.get('error')
        return HttpResponse(f"Error: {error}")


def analyze_genre_mood(genres):
    """Map genres to mood characteristics"""
    mood_map = {
        'happy': ['pop', 'dance', 'funk', 'disco', 'reggae', 'tropical'],
        'intense': ['metal', 'rock', 'punk', 'hardcore', 'grunge', 'industrial'],
        'chill': ['jazz', 'classical', 'ambient', 'lofi', 'acoustic', 'folk', 'new age'],
        'energetic': ['edm', 'electronic', 'workout', 'hip hop', 'trap', 'drill', 'house'],
        'emotional': ['soul', 'r&b', 'blues', 'indie', 'singer-songwriter', 'gospel'],
    }

    moods = {'happy': 0, 'intense': 0, 'chill': 0, 'energetic': 0, 'emotional': 0}

    for genre, count in genres:
        for mood, genre_list in mood_map.items():
            if any(g in genre.lower() for g in genre_list):
                moods[mood] += count

    return moods


def generate_face_from_taste(metrics, moods, genres):
    """Generate Notion face parameters from music taste"""

    explanation = {}

    # Ensure all values are within valid ranges
    skin = min(max(1, int(metrics['genre_diversity'] / 3)), 10)
    eyes = min(max(1, int(metrics['mainstream_score'] / 3)), 30)

    dominant_mood = max(moods, key=moods.get) if moods else 'neutral'
    mouth_map = {
        'happy': 25, 'intense': 8, 'chill': 15,
        'energetic': 20, 'emotional': 12
    }
    mouth = mouth_map.get(dominant_mood, 10)

    nose = min(max(1, int(metrics['loyalty_score'] * 20)), 20)
    hair = min(max(1, len(genres)), 30)
    accessories = min(int(metrics['explicit_preference'] * 10), 10)
    glasses = min(max(0, int((100 - metrics['avg_track_popularity']) / 5)), 20)
    eyebrows = min(max(1, int(moods.get('intense', 0) + moods.get('energetic', 0)) // 2), 15)

    # Build face params string
    face_params = f"s{skin}e{eyes}m{mouth}n{nose}h{hair}a{accessories}y{glasses}b{eyebrows}"

    # Add debug print
    print(f"Generated face params: {face_params}")

    # Create explanation...
    explanation['skin'] = f"Genre diversity ({metrics['genre_diversity']} genres) → {skin}"
    explanation['eyes'] = f"Mainstream score ({int(metrics['mainstream_score'])}%) → {eyes}"
    # ... rest of explanation

    return face_params, explanation