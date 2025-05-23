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
- **Persistence**: Database interaction layer

## Setup

1. Clone the repository
2. Create a `.env` file based on `.env.example`:
   ```
   API_KEY=your_lastfm_api_key
   API_SECRET=your_lastfm_api_secret
   LASTFM_USERNAME=your_lastfm_username
   LASTFM_PASSWORD=your_lastfm_password

   DATABASE_URL=postgresql://your_user:your_password@db:5432/your_db
   POSTGRES_DB=your_db
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   ```

## Docker usage

### Baked image

```bash
docker compose -f compose.yaml up --build -d
```
This setup uses a persistent volume for the Postgres data (pgdata), so data will persist across restarts, but any code changes will require re-baking the image.

### Development setup

```bash
docker compose -f compose.yaml -f dev.compose.yaml up --build -d
```
This starts ther app with `uvicorn --reload` and maps local source code into the container. Changes are reflected in real time.

### Local setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure Postgres is running and `DATABASE_URL` is configured.
3. Apply database migrations:
   ```bash
   alembic upgrade head
   ```
4. Start the app:
   ```bash
   uvicorn app.main:app -reload
   ```

## Database migrations

Alembic is used for schema migrations. Migration scripts are committed under `alembic/versions`.

To generate a new migration after schema changes:
```bash
alembic revision --autogenerate -m "message"
```

### Endpoints

- `GET /lastfm/scrobbles`: Fetch recent scrobbles
  - Query parameters:
    - `limit`: Optional. Maximum number of scrobbles to return

## Known Issues

- Business layer does not interact with persistence layer

This is intentional while I'm rewriting the persistence and business layers, methods are implemented but not connected yet.

- Data Transfer objects are coupled with persistence logic

This was a conscious decision, might consider creating a utility for this.

## Development Roadmap

#### 0.3.0
- ~~Create Dockerfile for containerization~~
- ~~Implement persistence layer~~

#### 0.4.0
- ~~Expand models as DTOs between layers~~
- ~~Persist timestamps~~
- (pushed back)Break down the repository layer into modules
- (pushed back)Break down the business layer into modules

#### 0.4.1
- Fix datbase connection concerns
- Implement custom exceptions

#### 0.?.?
- Write test suite
- Implement Importer service

## Dependencies

-fastapi\
-uvicorn\
-pylast\
-python-dotenv\
-pydantic\
-sqlalchemy\
-alembic\
-psycopg2-binary