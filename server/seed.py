#!/usr/bin/env python3

from datetime import date

from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():

    print("Clearing existing data...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Creating exercises...")

    push_up = Exercise(
        name="Push Up",
        category="Strength",
        equipment_needed=False
    )

    squat = Exercise(
        name="Squat",
        category="Strength",
        equipment_needed=False
    )

    bench_press = Exercise(
        name="Bench Press",
        category="Strength",
        equipment_needed=True
    )

    running = Exercise(
        name="Running",
        category="Cardio",
        equipment_needed=False
    )

    db.session.add_all([
        push_up,
        squat,
        bench_press,
        running
    ])

    db.session.commit()

    print("Creating workouts...")

    workout_1 = Workout(
        date=date(2026, 7, 20),
        duration_minutes=45,
        notes="Upper body strength workout"
    )

    workout_2 = Workout(
        date=date(2026, 7, 22),
        duration_minutes=30,
        notes="Lower body workout"
    )

    workout_3 = Workout(
        date=date(2026, 7, 24),
        duration_minutes=40,
        notes="Cardio and conditioning"
    )

    db.session.add_all([
        workout_1,
        workout_2,
        workout_3
    ])

    db.session.commit()

    print("Creating workout exercises...")

    workout_exercise_1 = WorkoutExercise(
        workout=workout_1,
        exercise=push_up,
        reps=15,
        sets=3,
        duration_seconds=None
    )

    workout_exercise_2 = WorkoutExercise(
        workout=workout_1,
        exercise=bench_press,
        reps=10,
        sets=4,
        duration_seconds=None
    )

    workout_exercise_3 = WorkoutExercise(
        workout=workout_2,
        exercise=squat,
        reps=12,
        sets=3,
        duration_seconds=None
    )

    workout_exercise_4 = WorkoutExercise(
        workout=workout_3,
        exercise=running,
        reps=1,
        sets=1,
        duration_seconds=1800
    )

    db.session.add_all([
        workout_exercise_1,
        workout_exercise_2,
        workout_exercise_3,
        workout_exercise_4
    ])

    db.session.commit()

    print("Database seeded successfully!")