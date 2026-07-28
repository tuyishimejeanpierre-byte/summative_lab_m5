from flask import Flask, make_response, request
from flask_migrate import Migrate

from models import db, Workout
from schemas import WorkoutSchema, WorkoutDetailSchema


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

if __name__ == "__main__":
    app.run(port=5555, debug=True)