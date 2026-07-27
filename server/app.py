from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Workout
from schemas import WorkoutSchema


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


if __name__ == "__main__":
    app.run(port=5555, debug=True)