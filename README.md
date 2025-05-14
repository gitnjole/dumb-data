# Dumb Data Backend

A Python FastAPI application to fetch and persist LastFM scrobble data from existing user accounts.

## Overview

This service connects to the LastFM API to retrieve listening history for a specified user account. It's designed to work alongside self-hosted music services and separate frontends, allowing you to maintain track listening data independently.

## Project Structure

The application follows a layered architecture with clear separation of concerns:

- **API Layer**: FastAPI endpoints for data retrieval
- **Business Layer**: Business logic processing
- **Client Layer**: Interaction with external LastFM API
- **Models**: Data transfer objects
- ~~**Persistence**: Database interaction layer~~ (Not yet implemented!)

## Setup

### Build from docker
1. Clone the repository
2. Create a `.env` file based on `.env.example`:
   ```
   API_KEY=your_lastfm_api_key
   API_SECRET=your_lastfm_api_secret
   LASTFM_USERNAME=your_lastfm_username
   LASTFM_PASSWORD=your_lastfm_password
   ```
3. Run `docker compose build`
4. Start docker
`docker compose up -d`

### Local setup
1. Clone the repository
2. Create a `.env` file based on `.env.example`:
   ```
   API_KEY=your_lastfm_api_key
   API_SECRET=your_lastfm_api_secret
   LASTFM_USERNAME=your_lastfm_username
   LASTFM_PASSWORD=your_lastfm_password
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```


## Usage

Start the application:
```
uvicorn app.main:app --reload
```

### Endpoints

- `GET /lastfm/scrobbles`: Fetch recent scrobbles
  - Query parameters:
    - `limit`: Optional. Maximum number of scrobbles to return

## Development Roadmap

- Implement persistence layer
- Expand models as DTOs between layers
- Write test suite
- Create Dockerfile for containerization

## Dependencies

- FastAPI
- pylast
- python-dotenv
- Pydantic