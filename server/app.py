from flask import Flask, make_response, request
from flask_migrate import Migrate

from models import db, Workout, WorkoutExercise, Exercise
from schemas import (
    WorkoutSchema,
    WorkoutDetailSchema,
    ExerciseSchema,
    ExerciseDetailSchema,
    WorkoutExerciseSchema
)


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    schema = WorkoutSchema(many=True)

    return make_response(
        schema.dump(workouts),
        200
    )
@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = db.session.get(Workout, id)

    if not workout:
        return make_response(
            {"error": "Workout not found"},
            404
        )

    schema = WorkoutDetailSchema()

    return make_response(
        schema.dump(workout),
        200
    )
@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json()

    schema = WorkoutSchema()

    try:
        workout_data = schema.load(data)
    except Exception as error:
        return make_response(
            {"errors": error.messages},
            400
        )

    workout = Workout(**workout_data)

    db.session.add(workout)
    db.session.commit()

    return make_response(
        schema.dump(workout),
        201
    )
@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = db.session.get(Workout, id)

    if not workout:
        return make_response(
            {"error": "Workout not found"},
            404
        )

    WorkoutExercise.query.filter_by(workout_id=id).delete()

    db.session.delete(workout)
    db.session.commit()

    return make_response(
        {"message": "Workout deleted successfully"},
        200
    )
@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()

    schema = ExerciseSchema(many=True)

    return make_response(
        schema.dump(exercises),
        200
    )
@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return make_response(
            {"error": "Exercise not found"},
            404
        )

    schema = ExerciseDetailSchema()

    return make_response(
        schema.dump(exercise),
        200
    )
@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.get_json()

    schema = ExerciseSchema()

    try:
        exercise_data = schema.load(data)
    except Exception as error:
        return make_response(
            {"errors": error.messages},
            400
        )

    exercise = Exercise(**exercise_data)

    db.session.add(exercise)
    db.session.commit()

    return make_response(
        schema.dump(exercise),
        201
    )
@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return make_response(
            {"error": "Exercise not found"},
            404
        )

    WorkoutExercise.query.filter_by(
        exercise_id=id
    ).delete()

    db.session.delete(exercise)
    db.session.commit()

    return make_response(
        {"message": "Exercise deleted successfully"},
        200
    )
@app.route(
    "/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises",
    methods=["POST"]
)
def add_exercise_to_workout(workout_id, exercise_id):
    workout = db.session.get(Workout, workout_id)
    exercise = db.session.get(Exercise, exercise_id)

    if not workout:
        return make_response(
            {"error": "Workout not found"},
            404
        )

    if not exercise:
        return make_response(
            {"error": "Exercise not found"},
            404
        )

    data = request.get_json()

    schema = WorkoutExerciseSchema()

    data["workout_id"] = workout_id
    data["exercise_id"] = exercise_id

    try:
        workout_exercise_data = schema.load(data)
    except Exception as error:
        return make_response(
            {"errors": error.messages},
            400
        )

    workout_exercise = WorkoutExercise(
        **workout_exercise_data
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return make_response(
        schema.dump(workout_exercise),
        201
    )

if __name__ == "__main__":
    app.run(port=5555, debug=True)