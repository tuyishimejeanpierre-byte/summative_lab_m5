#!/usr/bin/env python3

from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():

    # Seed data will be added later.
    pass