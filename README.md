# ⚠️ IN DEVELOPMENT

## NFWS(not nsfw): Notion Faces With Spotify
Creates Notion Face, a custom profile image, based on your music taste on Spotify. 

## Next Steps
- [X] Fetch and display user's top artists/tracks
- [ ] Categorize facial elements in Notion Faces
- [ ] Convert endpoint data to personal musical taste
- [ ] Map facial elements with musical taste
- [ ] Display output
- [ ] Set up a demo account and activate on Spotify Web API
- [ ] Polish docs and readme

## Dev Notes
### Limitations to Spotify API Development Mode, and its workaround
Spotify API no longer provides detailed audio features to individuals.
Therefore, I would have to come up with a custom model for deriving musical taste based on limited data.

### Available Enpoint Data
Available API Endpoints in Development Mode:

✅ User Profile Data
- User's display name, email, country, subscription type
- Profile images
- Follower count

✅ Listening History
- Top Artists - up to 50 artists for short/medium/long term
- Top Tracks - up to 50 tracks for short/medium/long term
- Recently Played - last 50 tracks played
- Track details: name, artist, album, popularity, duration, explicit flag, release date

✅ Artist Information
- Artist genres (this is key for your face mapping!)
- Artist popularity (0-100)
- Artist images
- Follower counts

✅ Playlists
- User's playlists
- Playlist tracks
- Collaborative playlist info

✅ Library
- Saved tracks
- Saved albums
- Saved shows/podcasts
- Following status for artists

✅ Search
- Search for tracks, artists, albums, playlists

### Data You Can Use for Face Generation:

Genre Analysis (from artists)
- Musical style diversity
- Dominant genres
- Niche vs mainstream genres


Popularity Metrics
- Artist popularity average
- Track popularity average
- Mainstream vs indie ratio


Listening Patterns
- Recent vs all-time favorites
- Artist loyalty (repeat artists)
- Discovery rate (new artists)


Time-based Preferences
- How your taste changes over time
- Seasonal patterns
- Consistency of preferences


Content Characteristics
- Explicit content ratio
- Release date patterns (old vs new music)
- Track duration preferences


Diversity Metrics
- Number of unique artists
- Number of unique genres
- Geographic diversity (artist countries)