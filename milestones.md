# Spotify Profile Picture Generator - Project Milestones

## Project Overview
A web application that generates personalized profile pictures using Notion faces based on user's Spotify listening history. Built with Python, Django, and Spotipy library.

## Notion Faces URL Parameter System
Base URL: `https://faces.notion.com/`

Parameter mapping:
- **s**: skin tone
- **e**: eyes
- **m**: mouth
- **n**: nose
- **h**: hair
- **a**: accessories
- **y**: glasses
- **b**: eyebrows

Example: `https://faces.notion.com/?face=s1e10m18n61h212a8y0b44`

---

## Milestone 1: Project Setup & Authentication

### Objectives
- Create a secure foundation for Spotify API integration
- Implement proper user authentication flow

### Tasks
- [ ] Initialize Django project with appropriate folder structure
- [ ] Create Django apps for `authentication`, `spotify_data`, and `image_generation`
- [ ] Register application on [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- [ ] Store Client ID and Client Secret in environment variables
- [ ] Implement Spotify OAuth 2.0 Authorization Code Flow
- [ ] Create user model to store Spotify tokens
- [ ] Build token refresh mechanism for expired access tokens
- [ ] Add logout functionality that revokes tokens

### Deliverables
- Working Spotify login/logout system
- Secure token storage and refresh mechanism

---

## Milestone 2: Data Collection from Spotify

### Objectives
- Gather comprehensive listening data from authenticated users
- Extract meaningful metrics for visual generation

### Tasks
- [ ] Set up Spotipy client with user authentication
- [ ] Implement data fetching for:
  - [ ] Top artists (short_term, medium_term, long_term)
  - [ ] Top tracks (short_term, medium_term, long_term)
  - [ ] Recently played tracks (last 50)
  - [ ] User's saved tracks sample
- [ ] Extract and store:
  - [ ] Audio features (energy, valence, danceability, acousticness, tempo)
  - [ ] Genre information from artists
  - [ ] Timestamp patterns for listening habits
  - [ ] Artist and track diversity metrics
- [ ] Create data models to cache fetched information
- [ ] Implement rate limiting compliance

### Deliverables
- Service layer for Spotify data retrieval
- Structured storage of user listening metrics

---

## Milestone 3: Music-to-Face Parameter Mapping Engine

### Objectives
- Create intelligent mapping between music characteristics and facial features
- Design algorithms that produce meaningful visual representations

### Tasks
- [ ] Document the full range of options for each Notion faces parameter
- [ ] Design mapping algorithms:

#### Feature Mapping Logic
| Feature | Parameter | Music Metric | Mapping Logic |
|---------|-----------|--------------|---------------|
| Skin tone | s | Time diversity | Different times of day = different tones |
| Eyes | e | Energy level | High energy = wide eyes, Low = relaxed |
| Mouth | m | Valence (happiness) | Happy music = smile, Sad = neutral/frown |
| Nose | n | Genre consistency | Consistent = straight, Diverse = unique |
| Hair | h | Primary genre | Rock/Electronic = wild, Classical/Jazz = neat |
| Accessories | a | Listening achievements | Milestones unlock accessories |
| Glasses | y | Acousticness | Acoustic/Instrumental = glasses |
| Eyebrows | b | Track intensity | Aggressive music = intense eyebrows |

- [ ] Create parameter calculation service
- [ ] Build face string generator (e.g., "s2e5m12n3h8a1y0b7")
- [ ] Implement variation algorithms for regeneration
- [ ] Add time-period based calculations (last month vs all-time)

### Deliverables
- Mapping algorithm documentation
- Parameter generation service
- Face URL builder

---

## Milestone 4: Face Generation & Enhancement

### Objectives
- Generate unique faces from Notion based on music data
- Enhance faces with Spotify statistics overlay

### Tasks
- [ ] Build Notion faces URL generator with calculated parameters
- [ ] Implement image fetching from faces.notion.com
- [ ] Create image enhancement service using Pillow:
  - [ ] Add username and generation date
  - [ ] Overlay top 3 artists or tracks
  - [ ] Display key statistics (hours listened, top genre)
  - [ ] Design Spotify-themed frames or badges
- [ ] Generate multiple image formats (square for profile, banner for headers)
- [ ] Implement image caching system
- [ ] Add watermark or app branding (optional)

### Deliverables
- Complete image generation pipeline
- Enhanced images with music statistics

---

## Milestone 5: User Interface

### Objectives
- Create intuitive and engaging user experience
- Provide customization options and insights

### Tasks
- [ ] Design and implement pages:
  - [ ] Landing page with Spotify login CTA
  - [ ] Dashboard showing music analysis
  - [ ] Generation page with live preview
  - [ ] Gallery of previously generated faces
- [ ] Build features:
  - [ ] Visual explanation of how features map to music
  - [ ] Time period selector (1 month, 6 months, all-time)
  - [ ] Manual parameter adjustment interface
  - [ ] Regenerate button for variations
  - [ ] Download options (with/without overlay)
  - [ ] Share buttons for social media
- [ ] Add loading states and progress indicators
- [ ] Implement error handling and user feedback

### Deliverables
- Fully functional web interface
- Responsive design for mobile and desktop

---

## Milestone 6: Optimization & Deployment

### Objectives
- Ensure scalable and reliable application performance
- Deploy to production environment

### Tasks
- [ ] Implement caching strategies:
  - [ ] Cache Spotify API responses (respect TTL)
  - [ ] Store generated face images
  - [ ] Cache Notion faces to reduce external calls
- [ ] Add background task processing with Celery for heavy operations
- [ ] Create user history system:
  - [ ] Store previously generated faces
  - [ ] Track listening evolution over time
  - [ ] Compare faces across time periods
- [ ] Performance optimizations:
  - [ ] Implement pagination for data fetching
  - [ ] Add request queuing for Notion faces
  - [ ] Optimize image processing
- [ ] Deployment preparation:
  - [ ] Set up production environment variables
  - [ ] Configure static file serving
  - [ ] Set up database (PostgreSQL recommended)
  - [ ] Implement logging and monitoring
  - [ ] Add analytics tracking

### Deliverables
- Production-ready application
- Deployment documentation
- Performance monitoring setup

---

## Technical Considerations

### Security
- Never expose Spotify API credentials
- Implement CSRF protection
- Use HTTPS in production
- Sanitize user inputs
- Implement rate limiting

### Scalability
- Consider CDN for static assets
- Implement database indexing
- Use connection pooling
- Monitor API quotas

### User Experience
- Provide clear explanations of how music maps to features
- Allow users to understand and control their data
- Implement proper error messages
- Add tutorial or onboarding flow

---

## Future Enhancements

1. **Social Features**
   - Compare faces with friends
   - Share musical DNA cards
   - Create group faces for shared playlists

2. **Advanced Analytics**
   - Listening mood throughout the day
   - Seasonal listening patterns
   - Genre evolution timeline

3. **Additional Customization**
   - Multiple face style options
   - Custom color schemes
   - Animation between time periods

4. **Integration Extensions**
   - Support for Apple Music
   - Last.fm integration
   - Export to NFT platforms

---

## Success Metrics

- User retention rate
- Number of faces generated
- Social media shares
- User feedback scores
- API efficiency (calls per generation)

---

## Timeline Estimate

- Milestone 1: 1 week
- Milestone 2: 1 week
- Milestone 3: 1-2 weeks
- Milestone 4: 1 week
- Milestone 5: 2 weeks
- Milestone 6: 1 week

**Total estimated time**: 7-8 weeks for MVP

---

*Last updated: September 2025*