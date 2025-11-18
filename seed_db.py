# seed_db.py
from models import StudySpot, db
from flask import Flask

def create_seed(app: Flask):
    """Seed the study spots database."""
    with app.app_context():
        # Check if database already has spots
        if StudySpot.query.first():
            return  # Already seeded

        study_spots_data = [
            {"name": "Central Library", "location": "Library", "seating": "Tables", "noise_level": "Quiet", "hours": "8am-10pm", "wifi_quality": "Strong"},
            {"name": "Campus Cafe", "location": "Cafe", "seating": "Couches", "noise_level": "Moderate", "hours": "7am-8pm", "wifi_quality": "Moderate"},
            {"name": "Engineering Hall Lounge", "location": "Engineering Hall", "seating": "Chairs", "noise_level": "Quiet", "hours": "9am-9pm", "wifi_quality": "Strong"},
            {"name": "Student Center", "location": "Student Center", "seating": "Tables", "noise_level": "Loud", "hours": "8am-11pm", "wifi_quality": "Weak"},
            {"name": "Art Building", "location": "Art Building", "seating": "Couches", "noise_level": "Quiet", "hours": "10am-6pm", "wifi_quality": "Moderate"},
        ]

        for s in study_spots_data:
            spot = StudySpot(
                name=s["name"],
                location=s["location"],
                seating=s["seating"],
                noise_level=s["noise_level"],
                hours=s["hours"],
                wifi_quality=s["wifi_quality"]
            )
            db.session.add(spot)

        db.session.commit()
        print("Database seeded successfully!")