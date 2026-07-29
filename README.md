# Flask SQLAlchemy Workout API

## Description

A Flask REST API for managing workouts and exercises.

The API allows users to:

- View, create, and delete workouts
- View, create, and delete exercises
- Add exercises to workouts
- Store reps, sets, and duration for workout exercises

The project uses Flask, SQLAlchemy, Flask-Migrate, Marshmallow, and SQLite.

## Technologies

- Python 3.8
- Flask 2.2.2
- Flask-SQLAlchemy 3.0.3
- Flask-Migrate 3.1.0
- Marshmallow 3.20.1
- SQLite
- Pipenv

## Project Structure

```text
summative_lab_m5/
├── README.md
├── Pipfile
├── Pipfile.lock
├── .gitignore
└── server/
    ├── app.py
    ├── models.py
    ├── schemas.py
    ├── seed.py
    ├── migrations/
    └── instance/
        └── app.db
Main Files
app.py - Flask application and API routes
models.py - Database models, relationships, constraints, and model validations
schemas.py - Marshmallow schemas and schema validations
seed.py - Creates sample database records
migrations/ - Database migration files
instance/app.db - SQLite database
Installation

Clone the repository:

git clone <your-github-repository-url>
cd summative_lab_m5

Install dependencies:

pipenv install

Activate the virtual environment:

pipenv shell
Database Setup

Move into the server directory:

cd server

Initialize migrations if needed:

pipenv run flask --app app:app db init

Create a migration:

pipenv run flask --app app:app db migrate -m "create database tables"

Apply the migration:

pipenv run flask --app app:app db upgrade
Seed the Database

Run:

pipenv run python seed.py

The seed file clears existing data and creates sample records for:

Exercises
Workouts
WorkoutExercises
Run the Application

From the server directory:

pipenv run python app.py

The API runs at:

http://127.0.0.1:5555

To view all registered routes:

pipenv run flask --app app:app routes
API Endpoints
Workouts
Method	Endpoint	Description
GET	/workouts	List all workouts
GET	/workouts/<id>	Show one workout and its exercises
POST	/workouts	Create a workout
DELETE	/workouts/<id>	Delete a workout
Exercises
Method	Endpoint	Description
GET	/exercises	List all exercises
GET	/exercises/<id>	Show one exercise and its workouts
POST	/exercises	Create an exercise
DELETE	/exercises/<id>	Delete an exercise
Workout Exercises
Method	Endpoint	Description
POST	/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises	Add an exercise to a workout

Example request:

{
  "reps": 10,
  "sets": 3,
  "duration_seconds": 30
}
Models
Exercise
id
name
category
equipment_needed
Workout
id
date
duration_minutes
notes
WorkoutExercise
id
workout_id
exercise_id
reps
sets
duration_seconds
Relationships
Workout has many WorkoutExercises
Exercise has many WorkoutExercises
WorkoutExercise belongs to Workout
WorkoutExercise belongs to Exercise
Workout has many Exercises through WorkoutExercises
Exercise has many Workouts through WorkoutExercises
Validations
Table Constraints

The database uses constraints including:

Primary keys
Required fields using nullable=False
Unique exercise names
Foreign keys
Required reps and sets
Model Validations

The models validate that:

Exercise names cannot be blank
Workout duration must be greater than 0
Reps must be greater than 0
Sets must be greater than 0
Duration seconds must be greater than 0 when provided
Schema Validations

Marshmallow validates:

Exercise name length
Exercise category length
Workout duration
Reps
Sets
Duration seconds
Serialization

Marshmallow is used to:

Serialize SQLAlchemy objects into JSON responses
Deserialize JSON requests into validated Python data
Validate incoming API data
Git Workflow

Git was used throughout development with meaningful commits for major features such as:

Models
Relationships
Constraints and validations
Migrations
Seed data
Schemas
API endpoints
README documentation
Author

Created as a Flask SQLAlchemy backend summative project.