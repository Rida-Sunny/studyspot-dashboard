# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, StudySpot
from seed_db import create_seed

app = Flask(__name__)
# Use absolute path for SQLite to avoid "unable to open database file"
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "instance", "studyspots.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supersecretkey"

db.init_app(app)

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def index():
    spots = StudySpot.query.all()
    return render_template("index.html", spots=spots)

@app.route("/dashboard")
def dashboard():
    spots = StudySpot.query.all()
    return render_template("dashboard.html", spots=spots)

@app.route("/search", methods=["POST"])
def search():
    location = request.form.get("location")
    noise = request.form.get("noise_level")
    wifi = request.form.get("wifi_quality")

    query = StudySpot.query
    if location:
        query = query.filter(StudySpot.location.ilike(f"%{location}%"))
    if noise:
        query = query.filter(StudySpot.noise_level == noise)
    if wifi:
        query = query.filter(StudySpot.wifi_quality == wifi)

    results = query.all()
    return render_template("dashboard.html", spots=results)

@app.route("/add_spot", methods=["GET","POST"])
def add_spot():
    if request.method == "POST":
        name = request.form.get("name")
        location = request.form.get("location")
        seating = request.form.get("seating")
        noise = request.form.get("noise_level")
        hours = request.form.get("hours")
        wifi = request.form.get("wifi_quality")

        if not name or not location:
            flash("Name and Location are required!")
            return redirect(url_for("add_spot"))

        spot = StudySpot(
            name=name,
            location=location,
            seating=seating,
            noise_level=noise,
            hours=hours,
            wifi_quality=wifi
        )
        db.session.add(spot)
        db.session.commit()
        flash("Study spot added!")
        return redirect(url_for("dashboard"))

    return render_template("add_spot.html")

# -----------------------------
# Run App and Seed DB
# -----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_seed(app)  # pass app to seed_db
    app.run(debug=True)