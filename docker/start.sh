#!/bin/sh
set -e

echo "Using DATABASE_URL: $DATABASE_URL"

dockerize -wait tcp://db:5432 -timeout 30s

alembic upgrade head

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
