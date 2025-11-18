#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=production
flask run --host=0.0.0.0 --port=$PORT
Flask==2.3.3
Flask-Login==0.6.3
Flask-Bcrypt==1.0.1
Flask-SQLAlchemy==3.0.3
python-dotenv==1.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.7