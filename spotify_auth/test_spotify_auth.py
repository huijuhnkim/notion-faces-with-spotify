import os
from django.test import TestCase
from django.conf import settings
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import spotipy


class SpotifyAuthTest(TestCase):
    def test_spotify_credentials_exist(self):
        """Test that Spotify credentials are properly loaded from environment"""
        print("\n" + "=" * 50)
        print("TEST 1: Checking Spotify Credentials")
        print("=" * 50)

        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

        self.assertIsNotNone(client_id)
        print(f"✓ Client ID found: {client_id[:10]}...")

        self.assertIsNotNone(client_secret)
        print(f"✓ Client Secret found: {client_secret[:10]}...")

        self.assertIsNotNone(redirect_uri)
        print(f"✓ Redirect URI found: {redirect_uri}")

        print("✅ All credentials successfully loaded from environment!")

    def test_spotify_oauth_object_creation(self):
        """Test that we can create a SpotifyOAuth object"""
        print("\n" + "=" * 50)
        print("TEST 2: Creating SpotifyOAuth Object")
        print("=" * 50)

        sp_oauth = SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
            scope='user-read-private user-read-email user-top-read'
        )

        self.assertIsNotNone(sp_oauth)
        print("✓ SpotifyOAuth object created successfully")

        self.assertEqual(sp_oauth.client_id, os.getenv('SPOTIFY_CLIENT_ID'))
        print(f"✓ Client ID correctly set in OAuth object")

        print(f"✓ Scope set to: {sp_oauth.scope}")
        print("✅ SpotifyOAuth object is properly configured!")

    def test_auth_url_generation(self):
        """Test that we can generate an authorization URL"""
        print("\n" + "=" * 50)
        print("TEST 3: Generating Authorization URL")
        print("=" * 50)

        sp_oauth = SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
            scope='user-read-private user-read-email'
        )

        auth_url = sp_oauth.get_authorize_url()

        self.assertIn('https://accounts.spotify.com/authorize', auth_url)
        print("✓ Authorization URL contains Spotify authorize endpoint")

        self.assertIn('client_id=' + os.getenv('SPOTIFY_CLIENT_ID'), auth_url)
        print("✓ Authorization URL contains correct Client ID")

        self.assertIn('redirect_uri=', auth_url)
        print("✓ Authorization URL contains redirect URI")

        print(f"\n📎 Generated Auth URL (first 100 chars):")
        print(f"   {auth_url[:100]}...")
        print("\n✅ Authorization URL generated successfully!")
        print("   You can use this URL to redirect users to Spotify login")

    def tearDown(self):
        """Print summary after each test"""
        print("-" * 50)