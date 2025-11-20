#!/bin/bash

# Use gunicorn to serve the Flask app on Render
export FLASK_APP=app.py
export FLASK_ENV=production

# Run gunicorn with 1 worker, listening on Render's $PORT
gunicorn --bind 0.0.0.0:$PORT app:app