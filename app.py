import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Default database (SQLite for local testing)
database_url = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class StudySpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(120), nullable=False)
    seating_capacity = db.Column(db.Integer, nullable=True)
    noise_level = db.Column(db.String(20), nullable=True)
    hours = db.Column(db.String(100), nullable=True)
    wifi_quality = db.Column(db.String(20), nullable=True)
    description = db.Column(db.Text, nullable=True)

@app.route('/')
def index():
    spots = StudySpot.query.all()
    return render_template('index.html', spots=spots)

@app.route('/search', methods=['POST'])
def search():
    noise = request.form.get('noise_level')
    wifi = request.form.get('wifi_quality')

    query = StudySpot.query
    if noise and noise != 'Any':
        query = query.filter_by(noise_level=noise)
    if wifi and wifi != 'Any':
        query = query.filter_by(wifi_quality=wifi)

    spots = query.all()
    return render_template('index.html', spots=spots)

if __name__ == '__main__':
    app.run(debug=True)