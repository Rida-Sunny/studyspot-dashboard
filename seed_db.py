from app import app, db, StudySpot

# Run inside the app context
with app.app_context():
    # Create the database tables
    db.create_all()

    # Add example study spots
    spots = [
        StudySpot(location_name="Library - Quiet Room", seating_capacity=20, noise_level="Quiet", hours="8am - 10pm", wifi_quality="Strong", description="Perfect for focused studying."),
        StudySpot(location_name="Student Center Lounge", seating_capacity=50, noise_level="Moderate", hours="9am - 11pm", wifi_quality="Average", description="Good for group study sessions."),
        StudySpot(location_name="Cafe Study Corner", seating_capacity=15, noise_level="Loud", hours="7am - 9pm", wifi_quality="Weak", description="Casual place to work with coffee."),
    ]

    for spot in spots:
        db.session.add(spot)

    db.session.commit()
    print("Database seeded successfully!")